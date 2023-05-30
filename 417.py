# Initial thoughts
    # Similar to other BFS/DFS problems but need to also condition on water levels
    # Start BFS/DFS from each point and see if it contains any 0's/4's, add to set
# Better approach
    # Graph traversal from all points takes (m*n)^2, so need to go faster
    # Instead of starting from each point, can alter traversal conditions and
        # start from each node on the border of the Pacific/Atlantic
    # Also DFS appears to work better
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, visited, prev_h):
            if r not in range(rows) or c not in range(cols) \
            or (r,c) in visited or heights[r][c] < prev_h:
                return
            visited.add((r,c))
            for i, j in directions:
                dfs(r + i, c + j, visited, heights[r][c])

        pac = set()
        atl = set()

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        res = []
        for i in pac:
            if i in atl:
                res.append(i)
        return res