# Initial thoughts
    # Can just do DFS from every node
    # Could also just do Union Find and could nodes with degree 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find_parent(v):
            parent = parents[v]
            while parent != parents[parent]:
                parent = parents[parents[v]]
                e = parents[v]
            return parent

        # Attempt to add edge to Union Find
        def union(v1, v2):
            p1 = find_parent(v1)
            p2 = find_parent(v2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for v1, v2 in edges:
            union(v1, v1)

        return len(set(parents))