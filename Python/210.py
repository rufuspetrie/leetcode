# Initial thoughts
    # Seems similar to the first course schedule problem, but you need to
        # find a path (topological order)
    # Repeat same process, but each time we find a node to have no prerequisites
        # remaining, we add it to the path
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[i].append(j)
        
        visiting = set()
        v = set()
        path = []
        def dfs(c):
            if c in visiting: 
                return False
            if c in v:
                return True
            visiting.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            v.add(c)
            path.append(c)
            visiting.remove(c)
            return True

        for c in graph:
            if not dfs(c):
                return []
        return path