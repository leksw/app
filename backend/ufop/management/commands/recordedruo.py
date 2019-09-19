from pathlib import Path
from xml.etree import ElementTree

from django.core.management.base import BaseCommand
from django.conf import settings


from ufop.models import Uo, Founder


class Command(BaseCommand):
    help = 'Records EDR UO data'

    def handle(self, *args, **options):
        tmp_dir = Path(settings.TMP_DATA_DIR)

        fop_file_list = [str(f) for f in tmp_dir.iterdir() if '_UO_' in str(f)]
        if fop_file_list:
            uo = Uo.objects.last()

            data_dict = {}
            founders = []
            context =  ElementTree.iterparse(fop_file_list[0], events=('start', 'end'))
            event, root = next(iter(context))
            on_record_tag = False
            on_founder_tag = False
            for event, elem in context:
                if event == 'start':
                    if elem.tag == "RECORD":
                        on_record_tag = True
                        is_record = True
                    else:
                        if on_record_tag:
                            if elem.tag == "FOUNDERS":
                                on_founder_tag = True
                                founders = []
                            else:
                                if on_founder_tag:
                                    elem_text = elem.text or ''
                                    founders.append(elem_text)

                            if elem.tag == 'STAN' and elem.text == 'припинено':
                                is_record = False

                            if not on_founder_tag:
                                elem_text = elem.text or ''
                                data_dict.update({elem.tag.lower(): elem_text})

                if event == 'end' and elem.tag == 'FOUNDERS':
                    on_founder_tag = False

                if event == 'end' and elem.tag == 'RECORD':
                    if is_record:
                        uo_record = uo.records.create(**data_dict)
                        for founder in founders:
                            fio, *share = founder.split(',')
                            uo_record.founders.create(fio=fio, share=', '.join(share))
                    data_dict.clear()
                    on_record_tag = False

                elem.clear()

        for tmp_file in tmp_dir.iterdir():
            if '_UO_' in tmp_file.name:
                tmp_file.unlink()
            
        self.stdout.write(self.style.SUCCESS('Successfully recorded "%s"' % Uo.objects.count()))
