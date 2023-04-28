# https://leetcode.com/problems/insert-interval/

# res = []
# newStart, newEnd = newInterval

# loop through intervals
# for each iteration
# start, end = interval
# if (newStart > end) -> not overlap -> res.append(interval)
# elif (newEnd < start) -> not overlap -> res.append(newInterval) -> res.append(the rest of intervals) -> return res
# else -> overlap -> update newInterval

# res.append(newInterval)
# return res


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start, end = interval

            # consider the "non-overlap" condition first!!!!!
            if newInterval[0] > end:  # newStart > end
                res.append(interval)
            elif newInterval[1] < start:  # newEnd < start
                res.append(newInterval)
                res += intervals[i:]
                return res

            # overlap condition -> update newInterval
            else:
                new_start = min(newInterval[0], start)
                new_end = max(newInterval[1], end)
                newInterval = [new_start, new_end]

        res.append(newInterval)
        return res


# O(N)
# O(1)
