import csv

csvInputFileName = "IT_Übung2"
csvOutputFileName = csvInputFileName + "_rowsfixed.csv"
csvInputFileName += ".csv"

csvInputFile = open(csvInputFileName, encoding="utf-8")
csvOutputFile = open(csvOutputFileName, 'w', newline='', encoding="utf-8")

# input = csv.reader(csvInputFile)
input = csv.reader(csvInputFile, delimiter=";", dialect="excel" )

fixedRows = list()

output = csv.writer(csvOutputFile, delimiter=";", dialect="excel")

for row in input:
    if row[2] == "2":
        print("Second line discovered! ( les", row[0], " zin", row[1], ")")
        fixedRows[-1][4] += " " + row[4]
        fixedRows[-1][5] += " " + row[5]
    else:
        fixedRows.append(row)

for row in fixedRows:
    if len(row[4]) != len(row[5]):
        print("!!!!!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!!!")
        print("Row[4] length: ", len(row[4]), "!= Row[5] length:", len(row[5]), " in les", row[0], " zin", row[1])
    output.writerow(row)
