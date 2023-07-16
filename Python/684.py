# Initial thoughts
    # Could do DFS solution and check whether each edge adds another
        # node to visited, but this will take O(v+e)^2
# Union Find
    # Union Find keeps track of the ranks and parents of all nodes as
        # you build a graph
    # When building the graph, you always make the node or subgraph with
        # higher rank (# of group members) the parent of ungrouped nodes
    # When adding a new edge to the Union Find, you can simply check the parent
        # of both nodes - if they're both in the graph, the edge is redundant
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # Helper function to find parent of a node
        def find_parent(e):
            parent = parents[e]
            while parent != parents[parent]:
                parent = parents[parents[e]]
                e = parents[e]
            return parent

        # Attempt to add edge to Union Find
        def union(e1, e2):
            p1 = find_parent(e1)
            p2 = find_parent(e2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]