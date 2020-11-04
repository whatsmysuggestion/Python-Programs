import csv

data = ['77', ' Danny2', ' New York55']

with open('people.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(data)

csvFile.close()