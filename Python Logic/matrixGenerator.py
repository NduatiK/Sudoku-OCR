from itertools import product

cols = "ABCDEFGHI"
rows = "123456789"
boxRowsGen=['ABC','DEF','GHI']
boxColumnsGen=['123','456','789']

matrix = dict()     
peers = dict()

def fillPeersDict():
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
    return peers

def fillMatrixDict():
    matrixGen = product(cols, rows)
    for a in range(81):
        cell = next(matrixGen)
        matrix["".join(cell)] = [str(a) for a in range(1, 10)]
    return matrix

def fillBoxPeersDict():
    boxMatrix = dict()
    # create 9 boxes
    for boxes in range(9):
        boxMatrix[boxes] = []
    n = -1
    # fill each box with consituent elements
    for boxRows in range(3):
        for boxColumns in range(3):
            n+=1
            
            boxValuesGen = product(boxRowsGen[boxRows],boxColumnsGen[boxColumns])
            for boxes in range(9):
                a = "".join(next(boxValuesGen))
                boxMatrix[n].extend([a])
    return boxMatrix
