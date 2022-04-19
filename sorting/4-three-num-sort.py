# solution 1. bucket sort
def threeNumberSort(array, order):
	bucket = [0, 0, 0]
	
	for num in array:
		if num == order[0]:
			bucket[0] += 1
		elif num == order[1]:
			bucket[1] += 1
		else:
			bucket[2] += 1
			
	i = 0
	while i < bucket[0]:
		array[i] = order[0]
		i += 1
	while i < sum(bucket[:2]):
		array[i] = order[1]
		i += 1
	while i < sum(bucket):
		array[i] = order[2]
		i += 1
		
	return array

# solution 2. three pointer
def threeNumberSort(array, order):
	first, second, third = 0, 0, len(array) - 1
	firstVal, secondVal = order[0], order[1]
	
	while second <= third:
		val = array[second]
		
		if val == firstVal:
			swap(array, first, second)
			first += 1
			second += 1
			
		elif val == secondVal:
			second += 1
			
		else:
			swap(array, second, third)
			third -= 1
			
	return array

def swap(array, p1, p2):
	array[p1], array[p2] = array[p2], array[p1]

# time: O(n)
# space: O(1)