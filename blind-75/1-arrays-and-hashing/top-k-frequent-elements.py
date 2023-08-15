# solution 1. (brute)
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hmap = defaultdict(int)
        freqs = []
        for num in nums:
            hmap[num] += 1
        
        for key, val in hmap.items():
            freqs.append([key, val])
        
        freqs = sorted(freqs, key=lambda freq:freq[1])
            
        for _ in range(k):
            key, val = freqs.pop()
            res.append(key)
        
        return res
    
# time: O(nlog(n))
# space: O(n)
# n: length of the nums

# ==============================================================================
# solution 2. (using heap)

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hmap = defaultdict(int)
        heap = []
        
        for num in nums:
            hmap[num] += 1
        for num, freq in hmap.items():
            heap.append([-freq, num])
        
        heapq.heapify(heap) # O(n)

        for _ in range(k):
            freq, num = heapq.heappop(heap) # O(log(n))
            res.append(num)
            
        return res
    
# time: O(klog(n))
# space: O(n)
# n: length of the nums

# ==============================================================================
# solution 3. (using bucket sort)

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hmap = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            hmap[num] += 1
        for num, freq in hmap.items():
            bucket[freq].append(num)
        
        for freq in range(len(bucket) - 1, -1, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
            
# time: O(n)
# space: O(n)
# n: length of the nums