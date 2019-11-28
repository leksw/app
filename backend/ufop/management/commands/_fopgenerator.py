from typing import Generator
from xml.etree import ElementTree


def create_fop_data_generator(file: str) -> Generator:
    context =  ElementTree.iterparse(file, events=('start', 'end'))
    event, root = next(iter(context))
    for event, elem in context:
        if event == 'start':
            if elem.tag == "RECORD":
                data_dict = {}
                on_record_tag = True
                is_record = True

            else:
                if on_record_tag:
                    if elem.tag == 'STAN' and elem.text == 'припинено':
                        is_record = False
                        continue
                    elem_text = elem.text or ''
                    data_dict.update({elem.tag.lower(): elem_text})

        if event == 'end' and elem.tag == 'RECORD':
            if is_record:
                yield data_dict
            on_record_tag = False

        elem.clear()
