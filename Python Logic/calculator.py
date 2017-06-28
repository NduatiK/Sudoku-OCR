from itertools import permutations as perm
import copy


def isTrueSudoku(matrix,allPeers):
    correctSudoku = True
    for grid in matrix.keys():
        for peer in allPeers[grid]:
            if matrix[grid] == matrix[peer]:
                correctSudoku = False
    return correctSudoku

def finalFix(matrix,matrix2,allPeers, boxPeers):
    notFailed = True
    for grid in matrix.keys():

        if not notFailed:
            return "No"
            break
        if len(matrix[grid]) == 2:
            p=matrix[grid][1]
            matrix[grid] = [matrix[grid][0]]
            notFailed = True
            while notFailed:

                sum1 = sum([len(a) for a in matrix.values()])
                matrix = scrubSingles(matrix, allPeers)
                matrix = scrubSpecialPairs(matrix, allPeers)
                matrix = scrubByElimination(matrix, allPeers, boxPeers)
                sum2 = sum([len(a) for a in matrix.values()])
                if sum1 == sum2:
                    notFailed = False
            if isTrueSudoku(matrix, allPeers):
                return matrix


            matrix2[grid] = [p]
            notFailed = True
            while notFailed:
                sum1 = sum([len(a) for a in matrix2.values()])
                matrix2 = scrubSingles(matrix2, allPeers)
                matrix2 = scrubSpecialPairs(matrix2, allPeers)
                matrix2 = scrubByElimination(matrix2, allPeers, boxPeers)
                sum2 = sum([len(a) for a in matrix2.values()])
                if sum1 == sum2:
                    notFailed = False
            if isTrueSudoku(matrix2,allPeers):
                return matrix2


    return "No"





def scrubSingles(matrix,allPeers):
    '''This method receives a matrix
    and removes the values of solved
    grids from its peers. Thus,
    impossible values are cleared away.


    :type matrix: dict()
    :type allPeers: dict()
     '''
    for key, value in matrix.items():

        if len(value) == 1:
            for peer in allPeers[key]:
                if value[0] in matrix[peer] and len(matrix[peer]) != 1:
                    matrix[peer].remove(value[0])
    return matrix



def scrubSpecialPairs(matrix,allPeers):
    '''This method receives a matrix
    and iterates through each grid.

    If a grid (1) has two possible values,
    the method finds out whether that grid
    has a peer (grid (2)) with the same value.

    The two values must exist in the
    grid (1) and grid (2) only among the peers
    they share. The method therefore removes
    these two values from the shared peer's
    possibilities


    :type matrix: dict()
    :type allPeers: dict()
     '''
    for grid, possibleValues in matrix.items():
        if len(possibleValues) == 2:

            # try to find a peer with the same 2 values
            for eachPeer in allPeers[grid]:
                if matrix[eachPeer] == possibleValues:

                    # find peers to both the grid and its equal peer
                    sharedPeers = sorted(list(set(allPeers[eachPeer]).intersection(allPeers[grid])))
                    for eachSharedPeer in sharedPeers:

                        # remove the special pair values from other grids
                        for val in matrix[grid]:
                            if val in matrix[eachSharedPeer]:
                                matrix[eachSharedPeer].remove(val)

    return matrix

def scrubByElimination(matrix,allPeers,boxPeers):
    '''This method receives a matrix
    and iterates through each grid in a specific box.

    By the process of elimination, it attempts
    to find where a specific digit MUST be.


    :type matrix: dict()
    :type allPeers: dict()
    :type boxPeers: dict()
     '''
    #for a specific box

    for boxLocation in boxPeers.keys():
        # search for values from 1 - 9
        for digit in range(1, 10):
            blockedPeers = dict()
            for grid in boxPeers[boxLocation]: #test if
                a = len(matrix[grid]) == 1 # Already has a set value (no need to test against digit it wont change)
                for peer in allPeers[grid]:
                        b = [str(digit)] == matrix[peer]    # A peer has this value (grid having digit is impossible)
                        if a or b :
                            blockedPeers[grid] = 'Blocked'

            numberOfBlockedPeers = 0

            for key,state in blockedPeers.items():
                if state == 'Blocked':
                    numberOfBlockedPeers+=1

            if numberOfBlockedPeers == 8:           #only one value is unblocked:
                for peer in boxPeers[boxLocation]:
                    if peer not in blockedPeers.keys():
                        matrix[peer] = [str(digit)]
    return matrix



def guessingGame(grid,matrix1,allPeers,boxPeers):
    '''If this method has been called then all hope has been lost and we are attempting random values

    :type matrix1: dict()
    :type grid: str()
     '''

    '''for useIndex in range(2):
        notFailed = True
        checkMatrix = copy.deepcopy(matrix1)
        checkMatrix[grid] = list(checkMatrix[grid][useIndex])

        while notFailed:
            sum1 = sum([len(a) for a in checkMatrix.values()])
            checkMatrix = scrubSingles(checkMatrix, allPeers)
            checkMatrix = scrubSpecialPairs(checkMatrix, allPeers)
            checkMatrix = scrubByElimination(checkMatrix, allPeers, boxPeers)
            sum2 = sum([len(a) for a in checkMatrix.values()])
            if sum1==sum2:
                if sum1 == 81:
                    return checkMatrix
                notFailed = False'''

    out = finalFix(copy.deepcopy(matrix1),copy.deepcopy(matrix1),allPeers, boxPeers)
    if type(out) == dict:
        return out
    else:
        return matrix1



