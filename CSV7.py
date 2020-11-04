import csv

csvData = [['SN', 'Items'], ['1', 'Pen'],
           ['2', 'Book'],
           ['3', 'Copy']]

csv.register_dialect('myDialect',delimiter = '|',quotechar = '^',
                     quoting=csv.QUOTE_ALL)

with open('quotechars.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, dialect='myDialect')
    writer.writerows(csvData)

print("writing completed")

csvFile.close()