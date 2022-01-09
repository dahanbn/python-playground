import csv

csvInputFileName = "IT_Übung2" + "_rowsfixed"
csvOutputFileName = csvInputFileName + "_processed.csv"
csvInputFileName += ".csv"

csvInputFile = open(csvInputFileName, encoding="utf-8")
csvOutputFile = open(csvOutputFileName, 'w', newline='', encoding="utf-8")

clozeBegin = "{{c1::"
clozeEnd = "}}"

input = csv.reader(csvInputFile, delimiter=";", dialect="excel")

output = csv.writer(csvOutputFile, delimiter=";", dialect="excel")

for row in input:
    if input.line_num == 1:
        # adding header CSentenceProcessed for the first row
        row.append("CSentenceProcessed")
    else:
        # need to process the following fields of a row:
        # field 4: CSentenceMask#
        # field 5: CSentenceSolutionAll
        processedSentence = ""
        for i in range(len(row[4])):
            # special case, sentence begins with #
            if i == 0 and row[4][i] == "#":
                processedSentence += clozeBegin
            # checking if it's a cloze begin mid sentence
            elif i > 0 and row[4][i] == "#" and row[4][i - 1] != "#":
                processedSentence += clozeBegin

            processedSentence = processedSentence + row[5][i]
#            print (i, len(row[4]), len(row[5]),processedSentence)
#            print(row[5])
#            print(row[4])
            # checking for the end of the cloze
            if row[4][i] == "#":
                # it's the last char in row[4]
                if i == len(row[4]) - 1:
                    processedSentence += clozeEnd
                # next character isn't an #
                elif row[4][i + 1] != "#":
                    processedSentence += clozeEnd

        row.append(processedSentence)

    output.writerow(row)
