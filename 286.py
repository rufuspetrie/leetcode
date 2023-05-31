# Initial thoughts
    # Need minimum distance, so probably want to use BFS
    # Want to avoid doing BFS on entire array ==> start from gates
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        rows = len(rooms)
        cols = len(rooms[0])        
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        def check_room(r,c):
            if r not in range(rows) or c not in range(cols) \
            or (r,c) in visited or rooms[r][c] == -1:
                return
            visited.add((r,c))
            queue.append((r,c))

        dist = 0
        while queue:
            # Slick move - iterate over length of queue to keep
                # track of the current search depth w/o arg, queues
            for i in range(queue):
                r, c = queue.popleft()
                rooms[r][c] = 0
                for i, j in dirs:
                    check_room(r + i, c + j)
            dist += 1