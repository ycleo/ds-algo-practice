# https://leetcode.com/problems/rotate-array
#         0  1. 2. 3. 4. 5. 6
# nums = [1, 2, 3, 4, 5, 6, 7]
# res =  [0, 0, 0, 0, 0, 0, 0]
# res =  [         1, 2, 3, 4]
# res =  [5, 6, 7, 1, 2, 3, 4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[(i + k) % len(nums)] = nums[i]

        nums[:] = res
# O(N)
# O(N)

# We use slice assignment (nums[:] = ...) to modify nums in place because it creates a view of the entire list and assigns the new values to this view, effectively replacing the original list with the new values.

# If we used simple assignment (nums = ...) instead, it would create a new reference to the new list and assign it to the variable nums. However, this would not modify the original list object and any other references to the original list would still point to the unmodified list.

# By using slice assignment, we are able to modify the original list object in place, while preserving any references to the list that may exist outside the function scope. This ensures that any changes made to the list inside the function are visible to the caller of the function.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        # 1. reverse all numbers
        reverse(0, n - 1)
        # 2. reverse first k elements
        reverse(0, k - 1)
        # 3. reverse last n - k elements
        reverse(k, n - 1)
# O(N)
# O(1)
