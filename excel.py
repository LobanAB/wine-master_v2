import pandas
import xlrd

excel_data = pandas.read_excel('wine.xlsx', sheet_name='Лист1').to_dict(orient='record')

print(excel_data)
