def bubbleSort(array):
    # Write your code here.
	for i in range(len(array) - 1, 0, -1):
		isSorted = True
		for j in range(i):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				isSorted = False
		if isSorted:
			return array		
	return array

# time: best: Ω(n), worst: O(n^2), avg: Θ(n^2)
# space: O(n)