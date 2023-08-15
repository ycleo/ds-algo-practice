# approach 1: DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for hor, ver in dirs:
                dfs(r + hor, c + ver)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
# time: O(m * n)
# space: O(max(m, n))

# approach 2: Union Find


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        self.numIslands = sum(
            grid[r][c] == "1" for r in range(ROW) for c in range(COL))
        parent = [i for i in range(ROW * COL)]
        rank = [0] * (ROW * COL)

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])  # path compression
            return parent[a]

        def union(a, b):
            aRoot, bRoot = find(a), find(b)
            if aRoot == bRoot:
                return

            # Union by Rank
            if rank[aRoot] < rank[bRoot]:
                aRoot, bRoot = bRoot, aRoot
            parent[bRoot] = aRoot
            rank[aRoot] += rank[bRoot]
            self.numIslands -= 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "0":
                    continue
                i = r * COL + c

                # check the direction "right" spot
                if c + 1 < COL and grid[r][c + 1] == "1":
                    union(i, i + 1)
                # chaeck the direction "down" spot
                if r + 1 < ROW and grid[r + 1][c] == "1":
                    union(i, i + COL)

        return self.numIslands
