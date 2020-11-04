import csv
data=[{'Grade': 'B', 'Name': 'Alex'},
      {'Grade': 'A', 'Name': 'Bin'},
      {'Grade': 'C', 'Name': 'Tom'}]

csv.register_dialect('myDialect',
                     delimiter = '|', quoting=csv.QUOTE_ALL)

with open('grade.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,dialect="myDialect")
    writer.writeheader()
    writer.writerows(data)
print("writing completed")
csvfile.close()