import sys
import zipfile
import calendar
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

import requests
from lxml import html
from dateutil import parser

from ufop.models import Uo, Fop


UKR_MONTHS = (
    'Січень', 'Лютий', 'Березень',
    'Квітень', 'Травень', 'Червень',
    'Липень', 'Серпень', 'Вересень',
    'Жовтень', 'Листопад', 'Грудень'
)
MONTH_DICT = dict(zip(UKR_MONTHS, tuple(calendar.month_name)[1:]))


class Command(BaseCommand):
    help = 'Upload EDR FOP and UO data'

    def handle(self, *args, **options):
        data_url = 'https://data.gov.ua/dataset/1c7f3815-3259-45e0-bdf1-64dca07ddc10/resource/b0476139-62f2-4ede-9d3b-884ad99afd08'
        
        try:
            page = requests.get(data_url)
        except requests.exceptions.RequestException as err:
            self.stdout.write(self.style.ERROR('%s' % err))
            sys.exit(1)
        
        tree = html.fromstring(page.content)
        ukr_date_update = next(iter(tree.xpath('//*[@id="content"]/div[2]/div/div[1]/table/tbody/tr[1]/td/text()')), None)
        file_url = next(iter(tree.xpath('//*[@id="content"]/div[2]/section/div[1]/p[2]/a/@href')), None)

        if ukr_date_update is None:
            self.stdout.write(self.style.ERROR('Update date is not found'))
            sys.exit(1)

        if data_url is None:
            self.stdout.write(self.style.ERROR('Zip file url is not found'))
            sys.exit(1)

        zip_file = Path('data.zip')
        tmp_dir = Path(settings.TMP_DATA_DIR)

        try:
            response = requests.get(file_url, stream=True)
        except requests.exceptions.RequestException as err:
            self.stdout.write(self.style.ERROR('%s' % err))
            sys.exit(1)

        with open(zip_file, 'wb') as target:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:
                    target.write(chunk)

        if zipfile.is_zipfile(str(zip_file)):
            with zipfile.ZipFile(str(zip_file), 'r') as zip_ref:
                zip_ref.extractall(tmp_dir)
            zip_file.unlink()
        else:
            self.stdout.write(self.style.ERROR('%s is not zip file' % zip_file))
            sys.exit(1)

        ukr_date_list = ukr_date_update.split(' ')
        ukr_date_list[0] = MONTH_DICT.get(ukr_date_list[0])
        ukr_date_list[-1] = 'UTC+3'
        update_date = parser.parse(' '.join(ukr_date_list))
        Uo.objects.get_or_create(update_date=update_date)
        Fop.objects.get_or_create(update_date=update_date)
            
        self.stdout.write(self.style.SUCCESS('Data is uploaded - ' % ukr_date_update))
