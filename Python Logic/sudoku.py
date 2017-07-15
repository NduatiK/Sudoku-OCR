import matrixGenerator
import calculator as calc
import populateMatrix

joiner3 = []
matrix = dict()     # will store allowed values for each grid coordinate(key)
allPeers = dict()      # will store all grid coordinates(value) that intersect with the each grid coordinate(key)




    # Create Dictionary of matrix of size 81

filename="a.txt"

matrix = matrixGenerator.fillMatrixDict()
allPeers = matrixGenerator.fillPeersDict()
boxPeers = matrixGenerator.fillBoxPeersDict()
matrix = populateMatrix.readFromFile(filename,matrix,splitter="|")
trys = 2
sum2 = 0
shouldExitGuessing = False
while sum([len(a) for a in matrix.values()]) != 81:  # stop only when finished
    print(".")
    sum1 = (sum([len(a) for a in matrix.values()]))
    matrix = calc.scrubSingles(matrix,allPeers)
    matrix = calc.scrubSpecialPairs(matrix,allPeers)
    matrix = calc.scrubByElimination(matrix,allPeers,boxPeers)
    print(sum1,sum2)
    sum2 = (sum([len(a) for a in matrix.values()]))
    if sum1 == sum2 and sum1 != 81: #all else has failed
        shouldExitGuessing = False
        for grid in matrix.keys():
            #if shouldExitGuessing: break
            if len(matrix[grid]) == trys:
                for peer in allPeers[grid]:
                    matrix = calc.guessingGame(grid, matrix, allPeers, boxPeers,trys)
                    shouldExitGuessing = True
                    break
        trys += 1




outputMatrix = ([val for key, val in matrix.items()])
for a in range(9):
    for b in range(9):
        print(outputMatrix[a+b*9][0],"\t",end='')
    print()
print(calc.isTrueSudoku(matrix,allPeers))
