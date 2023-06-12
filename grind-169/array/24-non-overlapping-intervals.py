# https://leetcode.com/problems/non-overlapping-intervals/submissions/
# sorting + greedy

# sort intervals based on the "end time"
# loop through intervals:
#   case 1: non-overlap -> prev = curr
#   case 2: overlap -> remove++ (remove curr)

# if two intervals are overlapping, we want to remove the interval that has the longer end point
# Greedy: bc the longer interval will always overlap with more or the same number of future intervals compared to the shorter one

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda it: it[1])

        remove = 0
        prevEnd = float("-inf")
        for start, end in intervals:
            if start >= prevEnd:  # non-overlap
                prevEnd = end
            else:
                remove += 1

        return remove

# O(NlogN)
# O(1)
