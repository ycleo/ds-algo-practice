def twoSum(array, target):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == target:
                return [firstNum, secondNum]
    return []

# time: O(n^2)
# space: O(1)