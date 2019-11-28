import time
from pathlib import Path


from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

from ufop.models import Fop
from ._stringIteratorio import StringIteratorIO, clean_csv_value
from ._fopgenerator import create_fop_data_generator


class Command(BaseCommand):
    help = 'Upload EDR FOP and UO data'

    def handle(self, *args, **options):
        tmp_dir = Path(settings.TMP_DATA_DIR)
        fop_file_list = [str(f) for f in tmp_dir.iterdir() if '_FOP_' in str(f)]

        if fop_file_list:
            fop = Fop.objects.last()
            start = time.perf_counter()
            data_generator = create_fop_data_generator(fop_file_list[0])

            with connection.cursor() as cursor:
                data_string_iterator = StringIteratorIO((
                    '|'.join(map(clean_csv_value, (
                        index,
                        obj['fio'],
                        obj['address'],
                        obj['kved'],
                        obj['stan'],
                        fop.id
                    ))) + '\n'
                    for index, obj in enumerate(data_generator, start=1)
                ))
                cursor.copy_from(data_string_iterator, 'ufop_foprecord', sep='|')
       
            elapsed = time.perf_counter() - start
        # for tmp_file in tmp_dir.iterdir():
        #     if '_FOP_' in tmp_file.name:
        #         tmp_file.unlink()

        self.stdout.write(self.style.SUCCESS('Successfully recorded "%s" - %s' % (fop.records.count(), f'{elapsed:0.4}')))
