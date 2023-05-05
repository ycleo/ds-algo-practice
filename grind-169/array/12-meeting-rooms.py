# https://leetcode.com/problems/meeting-rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i - 1]
            start, end = intervals[i]

            if prev_end > start:
                return False
        return True

# O(N)
# O(1)
