# solution 1.
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = array[i]**2
    
    return sorted(array)

# O(nlog(n)) time | O(1) space

# ============================================

# solution 2.
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallValIdx = 0
    bigValIdx = len(sortedSquares) - 1

    for idx in reversed(range(len(array))):
        smallVal = array[smallValIdx]
        bigVal = array[bigValIdx]

        if abs(smallVal) > abs(bigVal):
            sortedSquares[idx] = smallVal**2
            smallValIdx += 1
        else:
            sortedSquares[idx] = bigVal**2
            bigValIdx -= 1

    return sortedSquares

# O(n) time | O(n) space