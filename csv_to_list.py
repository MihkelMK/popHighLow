import csv
import re
from random import randint

def csvToDict(faile):
    f=open(faile, newline='',encoding="utf8")
    reader = csv.reader(f)
    inimesed=[]

    for row in reader:
        inimesed.append(row)
    f.close()
    dictionary={}

    for i in range(25):
        el = randint(0, len(inimesed)-1)
        if inimesed[el][3] != "":
            sõbrad=int(re.findall("[0-9]+", inimesed[el][3])[0])
            dictionary[inimesed[el][2]]=[sõbrad,inimesed[el][1]]
    return dictionary
