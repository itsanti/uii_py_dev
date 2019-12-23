from datetime import datetime
from docxtpl import DocxTemplate
from lib import get_data


def generate_report(data, template):
    context = {
        'report_date': datetime.now().date(),
        'cars': data
    }
    template = DocxTemplate(template)
    template.render(context)
    report_name = f'report_{context["report_date"]}.docx'
    template.save(report_name)
    return report_name


def add_gen_time(seconds, template):
    context = {
        'gen_time': seconds
    }
    tpl = DocxTemplate(template)
    tpl.render(context)
    tpl.save(template)


data = get_data('cars.txt')

start = datetime.now()
report_name = generate_report(data, 'cars_report_tpl.docx')
delta = datetime.now() - start
add_gen_time(delta.microseconds / 1000, report_name)
