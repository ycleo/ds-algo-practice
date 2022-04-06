# 1. Sort the array
# 2. set two pointers at the both ends of the array
# 3. while left < right 
	# sum = left + right values
	# if sum < target  ->  left++
	# eles if sum > target  ->  right--
	# else return left and right values
# 4. return empty array

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

# time: O(nlog(n))
# space: O(1)