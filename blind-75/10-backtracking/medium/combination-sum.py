class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(candiIdx, comb, combSum):
            if combSum == target:
                res.append(comb.copy())
                return
            if candiIdx >= len(candidates) or combSum > target:
                return
            
            comb.append(candidates[candiIdx])
            backtrack(candiIdx, comb, combSum + candidates[candiIdx])
            comb.pop()
            backtrack(candiIdx + 1, comb, combSum)
        
        backtrack(0, [], 0)
        return res
    
# time: O(2 ^ target)