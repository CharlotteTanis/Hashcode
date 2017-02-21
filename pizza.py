import csv

fp = "small.csv"

def Preparefile(fp, column):
    pizza = {}

    with open(fp, "rb") as filePizza:

        reader_ingredients = csv.reader(filePizza, delimiter=',')

        r = 0

        for ingredients in reader_ingredients:
            for c in range(0, column):
                pizza[(r, c)] = ingredients[c]
            r += 1

    for i in range(0, 6):
            print pizza[(i,0)], pizza[(i,1)], pizza[(i,2)], pizza[(i,3)], pizza[(i,4)], pizza[(i,5)], pizza[(i,6)]


Preparefile(fp, 7)