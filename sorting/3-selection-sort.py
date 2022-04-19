def selectionSort(array):
    for i in range(len(array) - 1):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j

        array[i], array[minIdx] = array[minIdx], array[i]

    return array

# time: best: Ω(n^2) avg: Θ(n^2) wrost: O(n^2)
# space: O(1)