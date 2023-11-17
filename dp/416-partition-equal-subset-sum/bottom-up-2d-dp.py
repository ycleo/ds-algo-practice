class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2

        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        # row i: partition includes nums[:i]
        # col j: sub sum
        # we want to get dp[n][target]

        dp[0][0] = True  # we can get 0 sub sum by empty partition

        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(target+1):
                if num > j:  # we definitely don't pick nums[i]
                    dp[i][j] = dp[i-1][j]
                else:
                    # not pick or pick nums[i]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]

        return dp[n][target]

# TC: O(n*target)
# SC: O(n*target)
