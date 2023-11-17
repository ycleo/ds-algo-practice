class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            dp2 = [False for _ in range(target + 1)]
            for j in range(target + 1):
                if num > j:
                    dp2[j] = dp[j]
                else:
                    dp2[j] = dp[j] or dp[j - num]
            dp = dp2

        return dp[target]
# TC: O(n*target)
# SC: O(target)

# ============================================================================
# think process: it always calculate using left part


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            for j in range(target, 0, -1):
                if num <= j and dp[j - num]:
                    dp[j] = True

        return dp[target]
# TC: O(n*target)
# SC: O(target)
