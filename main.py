from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
import argparse

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day
today = datetime.datetime(year=now_year, month=now_month, day=now_day)
estimate = datetime.datetime(year=1920, month=1, day=1)
delta_years = today.year - estimate.year

parser = argparse.ArgumentParser(
    description='Программа генерирует шалон сайта на основании xlsx таблицы'
)
parser.add_argument('-f', '--file', help='Имя файла с расширением xlsx')
args = parser.parse_args()
if args.file is None:
    excel_file = 'wine3.xlsx'
else:
    excel_file = args.file

excel_data = pandas.read_excel(excel_file, sheet_name='Лист1', keep_default_na=False).to_dict(orient='index')
output = collections.defaultdict(list)

for wine in excel_data.values():
    output[wine['Категория']].append(wine)

template = env.get_template('template.html')
rendered_page = template.render(
    date_delta=delta_years,
    wines=output,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
