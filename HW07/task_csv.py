from datetime import datetime
from lib import get_data
import csv


def generate_report(data):
    report_name = f'report_{datetime.now().date()}.csv'
    fields = data[0].keys()
    with open(report_name, 'w', encoding='utf=8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    return report_name


def add_gen_time(seconds, report_name):
    with open(report_name, 'a', encoding='utf=8') as f:
        f.write(f'\nвремя, затраченное на генерацию отчета: {seconds} мс')


data = get_data('cars.txt')

start = datetime.now()
report_name = generate_report(data)
delta = datetime.now() - start
add_gen_time(delta.microseconds / 1000, report_name)
