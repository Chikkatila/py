import csv
import io
import urllib.request
import pandas as pd
from openpyxl import Workbook


#url = 'https://docs.google.com/spreadsheets/d/13iy6bxHe41-0PPtBs6qFGy33GcBYocMS-YY2j7E25fg/export?format=csv'

#response = urllib.request.urlopen(url)

#with io.TextIOWrapper(response, encoding='utf-8') as f:
  #  reader = csv.reader(f)


df = pd.read_csv('https://docs.google.com/spreadsheets/d/13iy6bxHe41-0PPtBs6qFGy33GcBYocMS-YY2j7E25fg/export?format=csv')
#new_df = df[['col1', 'col2']]  # Выберем из датафрейма 2 столбца и сохраним в новый датафрейм
df.to_csv('output.csv', index=False) # Экспорт в CSV файл 
wb = Workbook()
ws = wb.active
with open('output.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('output.xlsx')
