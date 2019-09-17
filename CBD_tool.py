import csv

with open("C:\\Users\\hanns\\Desktop\\TwintCBDWorkfile.csv", 'r', encoding = "utf-8") as data:
    lines = data.readlines()
for i in range(len(lines)):
    print(lines[i])