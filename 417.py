# Initial thoughts
    # Similar to other BFS/DFS problems but need to also condition on water levels
    # Start BFS/DFS from each point and see if it contains any 0's/4's, add to set
# Better approach
    # Graph traversal from all points takes (m*n)^2, so need to go faster
    # Instead of starting from each point, can alter traversal conditions and
        # start from each node on the border of the Pacific/Atlantic
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        rows = len(heights)
        cols = len(heights[0])

        def bfs(r,c):
            pac = False
            atl = False
            visited = set()
            queue = deque()
            queue.append((r,c))

            while queue and (not pac or not atl):
                cr, cc = queue.popleft()
                if cr == 0 or cc == 0: pac = True
                if cr == rows - 1 or cc == cols - 1: atl = True
                visited.add((cr,cc))
                for dr, dc in directions:
                    xr, xc = cr + dr, cc + dc
                    if xr in range(rows) and xc in range(cols) \
                    and (xr, xc) not in visited and heights[xr][xc] <= heights[cr][cc]:
                        queue.append((xr,xc))

            return True if (pac and atl) else False

        res = []
        for r in range(rows):
            for c in range(cols):
                if bfs(r,c): res.append([r,c])
        
        return res