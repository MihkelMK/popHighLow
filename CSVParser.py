import csv
import re

def csvToDict(fail):
    inimesed=[]
    sõbrad={}

    with open(fail, newline='',encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            inimesed.append(row)
    
    for isik in inimesed:
        if isik[3] != "":
            ühised = int(re.findall("[0-9]+", isik[3])[0])
            sõbrad[isik[2]] = [ühised, isik[1]]
    return sõbrad