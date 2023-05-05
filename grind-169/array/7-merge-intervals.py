# https://leetcode.com/problems/merge-intervals/
# sorting + consider Non-overlap condition first !!!

# 0. sort intervals based on starting time
# 1. res = []
# 2. temp = intervals[0]

# 3. iterate the intervals[1:]:
# start, end = it
# if Non-overlap: temp_end < start  ->  push temp into res -> temp = it
# else (overlap) -> merge it into temp -> temp = [min(temp_start, start), max(temp_end, end)]

# 4. push temp into res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()  # O(nlogn)
        res = []
        temp = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            if temp[1] < start:
                res.append(temp)
                temp = interval
            else:
                temp = [min(temp[0], start), max(temp[1], end)]

        res.append(temp)
        return res

# O(NlogN)
# O(1)
