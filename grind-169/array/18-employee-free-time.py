# https://leetcode.com/problems/employee-free-time/submissions/

"""
# Definition for an Interval.
"""


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for s in schedule for i in s],
                           key=lambda i: i.start)
        res = []
        temp = intervals[0]

        for interval in intervals:
            if interval.start > temp.end:
                res.append(Interval(temp.end, interval.start))
                temp = interval
            else:
                temp.end = max(temp.end, interval.end)

        return res

# O(NlogN)
# O(N)
