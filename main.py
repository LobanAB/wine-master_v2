from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import xlrd

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

excel_data = pandas.read_excel('wine.xlsx', sheet_name='Лист1').to_dict(orient='record')


template = env.get_template('template.html')
rendered_page = template.render(
    date_delta=delta_years,
    wines=excel_data,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
