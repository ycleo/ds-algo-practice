# https://leetcode.com/problems/subarray-sum-equals-k
# prefix sum + hash map {prefix sum: duplicate prefix sum number}
# remember to add the initial prefix_sum {prefix_sum 0, duplicate 1} !!

# [1, 1, 1, 1], k = 2 -> 3
#  1  2  3  4

# prefix_sum = 0
# count = 0
# hash_map = {0: 1}

# loop through the array:
#   prefix_sum += nums[i]
#   if (prefix_sum - k) in map:
#       count += map[prefix_sum - k]

#   if prefix_sum not in map -> map[prefix_sum] = 1
#   else -> map[prefix_sum]++

# return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        hmap = {0: 1}  # prefix sum : prefix sum occur times

        for i, n in enumerate(nums):
            prefix_sum += n
            if prefix_sum - k in hmap:
                count += hmap[prefix_sum - k]

            if prefix_sum not in hmap:
                hmap[prefix_sum] = 1
            else:
                hmap[prefix_sum] += 1

        return count

# O(n)
# O(n)
