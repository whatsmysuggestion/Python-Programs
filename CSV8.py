import csv

data = [{'mountain' : 'Everest', 'height': '8848'},
      {'mountain' : 'K2 ', 'height': '8611'},
      {'mountain' : 'Kanchenjunga', 'height': '8586'}]

with open('peak.csv', 'w') as csvFile:

    fields = ['mountain', 'height']
    writer = csv.DictWriter(csvFile,
                            fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("writing completed")

csvFile.close()