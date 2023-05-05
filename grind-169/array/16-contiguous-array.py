# https://leetcode.com/problems/contiguous-array

# hash map + two indices that have the same count -> contiguous array
# remember to add the initial count {count 0, index -1} !!

# index     0   1   2   3   4   5   6   7
#          [0   0   1   0   0   0   1   1]
# count =  -1  -2  -1  -2  -3  -4  -3  -2

# maxLen = 0
# use a hash map to record the {count: smallest index}

# loop through the nums:
#   if 0 -> count--
#   if 1 -> count++

#   if count not in map -> add into map
#   else -> maxLen = max(maxLen, currentIndex - map[count])

# return maxLen

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        hmap = {0: -1}

        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count not in hmap:
                hmap[count] = i
            else:
                max_len = max(max_len, i - hmap[count])

        return max_len

# O(n)
# O(n)
