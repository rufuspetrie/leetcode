# Initial thoughts
    # Need to use directed graph to represent problem
    # [1,0], [0,1] fails because there is a cycle - use graph traversal to find it
    # DFS breakdown:
        # If c is in DFS path (visiting), return False
        # If c has no prerequisites, return True
        # If c has prerequisites, recursively check those
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[i].append(j)
        
        visiting = set()
        def dfs(c):
            if c in visiting: 
                return False
            if graph[c] == []:
                return True
            visiting.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            graph[c] = []
            visiting.remove(c)
            return True

        for c in graph:
            if not dfs(c):
                return False
        return True