import matrixGenerator
import calculator as calc

joiner3 = []
matrix = dict()     # will store allowed values for each grid coordinate(key)
allPeers = dict()      # will store all grid coordinates(value) that intersect with the each grid coordinate(key)




    # Create Dictionary of matrix of size 81

matrix = matrixGenerator.fillMatrixDict()
allPeers = matrixGenerator.fillPeersDict()
boxPeers = matrixGenerator.fillBoxPeersDict()


matrix["A1"]=['1']
matrix["A5"]=['7']
matrix["A7"]=['2']
matrix["A9"]=['4']
matrix["B2"]=['9']
matrix["C3"]=['5']
matrix["C5"]=['4']
matrix["C6"]=['8']
matrix["C7"]=['9']
matrix["C9"]=['1']
matrix["D4"]=['6']
matrix["D8"]=['9']
matrix["E1"]=['9']
matrix["E5"]=['2']
matrix["E9"]=['3']
matrix["F2"]=['4']
matrix["F6"]=['7']
matrix["G1"]=['2']
matrix["G3"]=['7']
matrix["G4"]=['1']
matrix["G5"]=['8']
matrix["G7"]=['3']
matrix["H8"]=['8']
matrix["I1"]=['6']
matrix["I3"]=['8']
matrix["I5"]=['9']
matrix["I9"]=['2']



print(sum([len(a) for a in matrix.values()]))

while sum([len(a) for a in matrix.values()]) != 81:  # stop only when finished
    matrix = calc.scrubSingles(matrix,allPeers)
    matrix = calc.scrubSpecialPairs(matrix,allPeers)
    matrix = calc.scrubByElimination(matrix,allPeers,boxPeers)
    print(sum([len(a) for a in matrix.values()]))

badOutputFormat = ([val for key, val in matrix.items()])
goodOutputFormat = []
for a in range(9):
    if a % 3 == 0:
        print ('-------------------+-------------------+--------------')
    for b in range(9):
        if b % 3 == 0:
            print(" | ",end='')
        print(" ",badOutputFormat[a+b*9][0]," ",end='')

    print()

