# https://leetcode.com/problems/meeting-rooms-ii/submissions/
# sorting based on start time + minHeap stores end time !!

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        res = 0

        intervals.sort()
        for start, end in intervals:
            while minHeap and start >= minHeap[0]:  # no need extra room
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
            res = max(res, len(minHeap))

        return res

# O(NlogN)
# O(N)
