# https://leetcode.com/problems/combination-sum/

# sorting + backtrack !!

# 1. sort the input array
# 2. perform backtrack
# if remain == 0  ->  add to res set -> return
# if i == len(candidates) or remain < 0  ->  return
# add the current number into comb
# keep consider current number, and update "remain"
# undo the comb
# don't consider current number, and keep the original "remain"


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(comb, i, remain):
            if remain == 0:
                res.append(comb.copy())
                return
            if i == len(candidates) or remain < 0:
                return

            comb.append(candidates[i])
            backtrack(comb, i, remain - candidates[i])
            comb.pop()
            backtrack(comb, i + 1, remain)

        backtrack([], 0, target)
        return res

# The time complexity of this algorithm depends on the number of solutions generated. In the worst case, the algorithm generates all possible combinations of the candidates array, which is exponential in the length of the array. Therefore, the time complexity is O(2^n), where n is the length of the candidates array.

# The space complexity is proportional to the maximum depth of the recursion tree, which is the length of the candidates array. Therefore, the space complexity is O(n), where n is the length of the candidates array.


# Similiar Problems:

# Subsets: https://leetcode.com/problems/subsets/
# Subsets II: https://leetcode.com/problems/subsets-ii/
# Permutations: https://leetcode.com/problems/permutations/
# Permutations II: https://leetcode.com/problems/permutations-ii/
# Combinations: https://leetcode.com/problems/combinations/
# Combination Sum II: https://leetcode.com/problems/combination-sum-ii/
# Combination Sum III: https://leetcode.com/problems/combination-sum-iii/
# Palindrome Partition: https://leetcode.com/problems/palindrome-partitioning/
