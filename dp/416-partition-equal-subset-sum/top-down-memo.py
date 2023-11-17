class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        half, remainder = divmod(sum(nums), 2)
        if remainder > 0:
            return False

        cache = {}  # (nums index, remain) -> bool

        def dfs(idx, remain):
            if remain == 0:
                return True
            if idx == n or remain < 0:
                return False
            if (idx, remain) in cache:
                return cache[(idx, remain)]

            cache[(idx, remain)] = dfs(
                idx+1, remain) or dfs(idx+1, remain-nums[idx])
            return cache[(idx, remain)]

        return dfs(0, half)

# TC: O(n * m)
# In the worst case where there is no overlapping calculation, the maximum number of entries in the memo would be m⋅n. For each entry, overall we could consider that it takes constant time

# SC: O(n * m) # m = half
# We are using a 2 dimensional array cache of size (m⋅n) and O(n) space to store the recursive call stack. This gives us the space complexity as O(n) + O(m⋅n) = O(m⋅n)
