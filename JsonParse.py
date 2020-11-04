import json
def loadRSS():
#https://www.w3schools.com/angular/customers.php
    data=open("topnewsfeed.json","rb")

    finaldata=json.load(data)
    #print(finaldata.get("records"))
    temp=finaldata.get("records")

    for i in temp:
        print(i.get('Name'))

loadRSS()