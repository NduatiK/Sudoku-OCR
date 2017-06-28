import re
from matrixGenerator import listOfGrids

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def readFromFile(filename,matrix,splitter):
    numbers = ""
    inputFile = open(filename,encoding='utf-8')
    lineCount = file_len(filename)

    numbersPattern = re.compile("^(\d{9})$")
    for lineNo in range(lineCount):
        inputLine = inputFile.readline()
        inputLine = "".join(inputLine.replace(" ","").split(splitter)).replace("\n","")
        found = numbersPattern.search(inputLine)
        if found:
            numbers = "".join([numbers,inputLine])
    inputFile.close()


    gridList = listOfGrids()
    for grid in range(81):
        if numbers[grid] != '0':
            matrix[gridList[grid]] = [numbers[grid]]
    return matrix
