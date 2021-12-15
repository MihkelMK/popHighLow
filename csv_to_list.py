import csv
import re

faile=input("Sisesta failinimi: ")
f=open(faile, newline='',encoding="utf8")
reader = csv.reader(f)
inimesed=[]

for row in reader:
    inimesed.append(row)
f.close()
dictionary={}

for el in range(len(inimesed)):
    if inimesed[el][3] != "":
        sõbrad=int(re.findall("[0-9]+", inimesed[el][3])[0])
        print(sõbrad, type(sõbrad))
        dictionary[inimesed[el][2]]=[sõbrad,inimesed[el][1]]
