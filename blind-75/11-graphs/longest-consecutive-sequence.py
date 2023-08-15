# approach 1: hash set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        res = 0

        for n in nums:
            if n - 1 in cache:
                continue
            temp = 0
            curr = n
            while curr in cache:
                temp += 1
                curr += 1
            res = max(res, temp)

        return res

# approach 2: union find


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.ret = 1
        parent = {n: n for n in nums}
        rank = {n: 1 for n in nums}

        def find(x):
            if x not in parent:
                return None
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            aRoot, bRoot = find(a), find(b)
            # Don't use "not aRoot" because there might be number 0
            if aRoot == None or bRoot == None or aRoot == bRoot:
                return

            if rank[aRoot] < rank[bRoot]:
                aRoot, bRoot = bRoot, aRoot
            parent[bRoot] = aRoot
            rank[aRoot] += rank[bRoot]
            self.ret = max(self.ret, rank[aRoot])

        for n in nums:
            union(n, n + 1)

        return self.ret
