# https://leetcode.com/problems/product-of-array-except-self/

# 1. Initialize an all 1 list "res" of the same length as the input list nums.
# 2. Initialize a variable prefix to 1.
# 3. Iterate through the input list nums and update each element of res as follows:
#     - Multiply the current element of res by prefix.
#     - Multiply prefix by the current element of nums.
#      (note) we need to update the "res" before update the prefix, so that we won't multiply the value of it self

# 4. Initialize a variable postfix to 1.
# 5. Iterate through the input list nums in reverse order and update each element of res as follows:
#     - Multiply the current element of res by postfix.
#     - Multiply postfix by the current element of nums.

# 6. Return the final list "res".

# nums = [1, 2, 3, 4]
# res = [1, 1, 1, 1]

# prefix = 1
# res = [1, 1, 2, 6]

# postfix = 1
# res = [24, 12, 8, 6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# O(N)
# O(1)
