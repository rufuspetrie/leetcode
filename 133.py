# Initial thoughts
    # Probably similar to making deep copy of linked list
    # Traverse graph once to extract the nodes
    # Traverse graph again to extact nodes into a hash
    # Traverse copy of graph and use hash to update neighbors
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        copies = {}

        def dfs(node):
            copies[node] = Node(node.val)
            for i in node.neighbors:
                if i and i not in copies:
                    dfs(i)

        dfs(node)
        for o, c in copies.items():
            for i in o.neighbors:
                copies[o].neighbors.append(copies[i])
            
        return copies[node]
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""