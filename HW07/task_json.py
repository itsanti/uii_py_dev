from datetime import datetime
from lib import get_data
import json


def generate_report(data):
    report_name = f'report_{datetime.now().date()}.json'
    with open(report_name, 'w', encoding='utf=8') as f:
        json.dump(data, f)
    return report_name


def add_gen_time(seconds, report_name):
    with open(report_name, 'r+', encoding='utf=8') as f:
        data = json.load(f)
        f.seek(0)
        json.dump({
            'gen_time': seconds,
            'data': data
        }, f)


data = get_data('cars.txt')

start = datetime.now()
report_name = generate_report(data)
delta = datetime.now() - start
add_gen_time(delta.microseconds / 1000, report_name)
