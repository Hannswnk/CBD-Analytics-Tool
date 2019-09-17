import csv

with open("C:\\Users\\hanns\\Desktop\\TwintCBDWorkfile.csv", 'r', encoding = "utf-8") as data:
    lines = data.readlines()
for i in range(len(lines)):
    print(lines[i])

def Tweet_Counter():
    counter = 0
    for tweet in lines:
        counter += 1
    print(counter - 2)