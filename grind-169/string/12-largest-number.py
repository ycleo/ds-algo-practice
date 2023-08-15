# https://leetcode.com/problems/largest-number

class LargerNum(str):
    def __lt__ (x, y):
        return x + y > y + x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str, nums), key=LargerNum))
        return '0' if res[0] == '0' else res