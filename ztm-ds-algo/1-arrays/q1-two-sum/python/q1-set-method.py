def twoNumberSum(array, targetSum):
	nums = set()
	for num in array:
		match = targetSum - num
		if match in nums:
			return [match, num]
		else:
			nums.add(num)
	return []

# space: O(n)
# time: O(n)