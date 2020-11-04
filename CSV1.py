import csv
row = ['6', ' dinesh3', ' California2']

with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[3] = row


with open('people2.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()