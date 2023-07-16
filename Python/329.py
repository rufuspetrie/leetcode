# Initial thoughts
    # Can use DFS with a cache to note path length at each cell
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        rows = len(matrix)
        cols = len(matrix[0])
        DP = {}

        def dfs(r, c, p):
            if r not in  range(rows) or c not in range(cols) or matrix[r][c] <= p:
                return 0
            if (r,c) in DP:
                return DP[(r,c)]

            res = 1
            for i, j in dirs:
                res = max(res, 1 + dfs(r + i, c + j, matrix[r][c]))
            DP[(r,c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(DP.values())