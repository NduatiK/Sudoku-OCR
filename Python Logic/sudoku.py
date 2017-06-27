S
from itertools import product

cols = "ABCDEFGHI"
rows = "123456789"
joiner3 = []
matrix = dict()
peers = dict()
matrixGen = product(cols, rows)
boxRowsGen=['ABC','DEF','GHI']
boxColumnsGen=['123','456','789']

boxMatrixPeers = dict()
for nos in range(9):
    boxMatrixPeers[nos] = []
n = -1
#print(boxMatrixPeers.items())
for boxRows in range(3):
    for boxColumns in range(3):
        n+=1
        boxGen = product(boxRowsGen[boxRows],boxColumnsGen[boxColumns])
        for nos in range(9):
            a = "".join(next(boxGen))
          #  print(a)
            boxMatrixPeers[n].extend([a])


print(boxMatrixPeers.items())


    # Create Dictionary of matrix
for a in range(81):
    cell = next(matrixGen)
    matrix["".join(cell)] = [str(a) for a in range(1, 10)]
    peers["".join(cell)] = []
for r in rows:
    for c in cols:
        peers["".join([c, r])] = ["".join([c2, r]) for c2 in cols]
        peers["".join([c, r])].extend(["".join([c, r2]) for r2 in rows])
        peers["".join([c, r])].extend(["".join([c, r2]) for r2 in rows])
        rangeC1 = cols.index(c) - cols.index(c) % 3 if cols.index(c) - cols.index(c) % 3 >= 0  else cols.index(c) % 3
        rangeC2 = cols.index(c) - cols.index(c) % 3 + 3 if cols.index(c) - cols.index(c) % 3 + 3 >= 0  else cols.index(
            c) % 3 + 3
        rangeR1 = rows.index(r) - rows.index(r) % 3 if rows.index(r) - rows.index(r) % 3 >= 0      else   rows.index(
            r) % 3
        rangeR2 = rows.index(r) - rows.index(r) % 3 + 3 if rows.index(r) - rows.index(
            r) % 3 + 3 >= 0     else rows.index(r) % 3 + 3
        for c3 in range(rangeC1, rangeC2):
            for r3 in range(rangeR1, rangeR2):
                joiner3 = ["".join([cols[c3], rows[r3]])]
                peers["".join([c, r])].extend(joiner3)
for key, value in peers.items():
    peers[key] = sorted(list(set(value)))
    peers[key].remove(key)
# print(matrix.items())
# print (peers.items())



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



def scrub(matrix):
    for key, value in matrix.items():

        if len(value) == 1:
            for peer in peers[key]:
                if value[0] in matrix[peer] and len(matrix[peer]) != 1:
                    matrix[peer].remove(value[0])
    return matrix


while sum([len(a) for a in matrix.values()]) != 81:  # stop only when finished
    print(sum([len(a) for a in matrix.values() if len(a)==1]))
    matrix = scrub(matrix)
    #print([(key,val)  for key, val in matrix.items() if len(val)==1])
    for coord, values in matrix.items():
        #print(coord)
        if len(values) == 0:
            print("Bad")
        if len(values) == 2:
            for peer in peers[coord]:
                if matrix[peer] == values:
                    sharedpeers = sorted(list(set(peers[peer]).intersection(peers[coord])))
                    for shared in sharedpeers:
                        for val in matrix[coord]:
                            if val in matrix[shared]:
                                matrix[shared].remove(val)
    print("Here")







    #in each box:
    for boxLocation in boxMatrixPeers.keys():

        #print("boxLo:",boxLocation)
        #check for all digits
        for count in range(1, 10):
       #     print("Count is ", count,"Box is",boxLocation)

            boxCompanionNo = dict()
            okay = False
            number = 0
            #in each box:
            for boxPeers in boxMatrixPeers[boxLocation]:
                #check if this box is okay for our count
                if [str(count)] == matrix[boxPeers]:
                    okay = True
                    break
            test =str()
            for boxPeers in boxMatrixPeers[boxLocation]:
                if okay == True: #if box has solved count, no need to fix
                    break
                else:
                 #   print("in")

                    #for all peers of box companions
                    for allPeers in peers[boxPeers]:

                        a = matrix[allPeers] == [str(count)]
                        b = len(matrix[boxPeers]) == 1
                        c = [str(count)] == matrix[allPeers]
                        #print(a, b, c,str(count),matrix[allPeers],allPeers,"\n",peers[boxPeers])
                        test = boxPeers
                        if a or b or c:
                            boxCompanionNo[boxPeers] = 'Blocked'
                           # if boxPeers == 'H1' and count == 8 and boxLocation == 6:
                            #    print(a,b,c)
                            #    print(str(count),matrix[allPeers],boxPeers)
                            #    print('WOOO'*10)
                             #   print(boxCompanionNo.items())

            count1 = 0
            for key,val in boxCompanionNo.items():
                if okay == True: #if box has solved count, no need to fix
                    break
                if val == 'Blocked':
                    count1+=1

            if count1 == 8:
                if okay == True: #if box has solved count, no need to fix
                    break
                #print(boxMatrixPeers[boxLocation])
                for boxPeers in boxMatrixPeers[boxLocation]:
                    #print("SOLVED SOMETHING")
                 #   print(boxPeers,matrix[boxPeers])
                    if boxPeers not in boxCompanionNo.keys():
                        matrix[boxPeers] = [str(count)]
                        print(boxPeers , [str(count)])


'''
if count == 9 and boxLocation == 6:
    print(test, matrix[test])
    print([(key, val) for key, val in matrix.items()])
    print(boxCompanionNo.items()'''













badOutputFormat = ([val for key, val in matrix.items()])
goodOutputFormat = []
for a in range(9):
    if a % 3 == 0:
        print ('-------------------+-------------------+--------------')
    for b in range(9):
        if b % 3 == 0: print(" | ", end='')
        print(" ",badOutputFormat[a+b*9][0]," ",end='')

    print()

