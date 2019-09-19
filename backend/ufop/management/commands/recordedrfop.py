from pathlib import Path
from xml.etree import ElementTree

from django.core.management.base import BaseCommand
from django.conf import settings

from ufop.models import Fop


class Command(BaseCommand):
    help = 'Upload EDR FOP and UO data'

    def handle(self, *args, **options):
        tmp_dir = Path(settings.TMP_DATA_DIR)

        fop_file_list = [str(f) for f in tmp_dir.iterdir() if '_FOP_' in str(f)]
        if fop_file_list:
            fop = Fop.objects.last()

            data_dict = {}
            context =  ElementTree.iterparse(fop_file_list[0], events=('start', 'end'))
            event, root = next(iter(context))
            for event, elem in context:
                if event == 'start':
                    if elem.tag == "RECORD" :
                        on_record_tag = True
                        is_record = True
                    else:
                        if on_record_tag:
                            if elem.tag == 'STAN' and elem.text == 'припинено':
                                is_record = False
                            elem_text = elem.text or ''
                            data_dict.update({elem.tag.lower(): elem_text})

                if event == 'end' and elem.tag == 'RECORD':
                    if is_record:
                        fop.records.create(**data_dict)
                    data_dict.clear()
                    on_record_tag = False
                elem.clear()

        for tmp_file in tmp_dir.iterdir():
            if '_FOP_' in tmp_file.name:
                tmp_file.unlink()
            
        self.stdout.write(self.style.SUCCESS('Successfully recorded "%s"' % fop.records.count()))
