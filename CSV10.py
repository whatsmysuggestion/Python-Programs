import csv
gender="male"
with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    for i in lines:
        if(i==0):
            print(i[0])
        else:
            print(i[0])
