import csv

csvData = [['Fruit', 'Quantity'],
           ['Apple', '5'],
           ['Orange', '7'],
           ['Mango', '8']]

csv.register_dialect('myDialect',
    delimiter = '|', lineterminator = '\n')

with open('lineterminator.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerows(csvData)

f.close()