# Monotonically Decreasing Queue (value, index)
# loop through the numms array
# if the new added number is bigger than the last value in the Queue => keep popping
# queue.append((new value, new index))
# check if the element index at the front of the queue is within current left border -> if not -> popleft to count it out
# if it's more than the kth iteration -> append the element value at the front of the queue -> left border ++

#         0  1   2   3  4
# nums = [1, 8, -1, -3, 5] k = 3
# output = [8, 8, 5]

# deq = [(1, 0)]  # (value, index)
# deq = [(8, 1), (-1, 2), (-3, 3)]
# deq = [(5, 4)]

import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        res = []
        left = 0

        for i, n in enumerate(nums):
            # keep popping the smaller value from the queue
            while deq and deq[-1][0] <= n:
                deq.pop()
            deq.append((n, i))  # push the current (value, index)

            if left > deq[0][1]:  # the maximum value in the deq locates out of the left border
                deq.popleft()    # count it out

            if i >= k - 1:
                res.append(deq[0][0])
                left += 1  # adjust the left border

        return res
# O(N)
# O(k) -> the deque will maintains no more than k elements by the left border
