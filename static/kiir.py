teeMaatriks = [
    [0,  1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10, 11],
    [12, 13, 14, 15, 16, 17]]

def kiir(maatriks, suund, teeList):
    while True:
        teeList.append([maatriks])

def tee(maatriks):

    try:
        print(maatriks[1][1])
        tee(maatriks[1:][1:])
    except:
        print(maatriks[0][0])

tee(teeMaatriks)