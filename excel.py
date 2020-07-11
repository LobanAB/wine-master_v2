import pandas
import xlrd
from pprint import pprint
import collections

excel_data = pandas.read_excel('wine3.xlsx', sheet_name='Лист1').to_dict(orient='index')

output = collections.defaultdict(dict)
#category = []
#for key, value in excel_data.items():
#    value['Категория']
#    category.append(value['Категория'])
#category = list(set(category))
for key, value in excel_data.items():
    output[value['Категория']][len(output[value['Категория']])] = value

pprint(output)

print(output.keys())
