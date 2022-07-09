
# solution 1. 

def twoNumberSum(array, targetSum):
    hashSet = set()

    for num in array:
        otherNum = targetSum - num
        if otherNum in hashSet:
            return [num, otherNum]
        hashSet.add(num)

    return []

# O(n) time | O(n) space

# =======================================================

# solution 2.
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
		else:
			return [array[left], array[right]]
	return []

# O(nlog(n)) time | O(1) space