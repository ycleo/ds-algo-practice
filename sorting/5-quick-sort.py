def quickSort(array):
	quickSorting(array, 0, len(array) - 1)
	return array

def quickSorting(array, left, right):
	if left < right:
		pivot = partition(array, left, right)
		quickSorting(array, left, pivot - 1)
		quickSorting(array, pivot + 1, right)

def partition(array, left, right):
	pivot = left
	for i in range(left, right):
		if array[i] < array[right]:
			array[i], array[pivot] = array[pivot], array[i]
			pivot += 1
	array[pivot], array[right] = array[right], array[pivot]
	return pivot

# time: best: Ω(n log(n)) avg: Θ(n log(n)) worst: O(n^2)
# space: O(log(n))

# Good Analysis Video: https://www.youtube.com/watch?v=k2xra5tS3Vs