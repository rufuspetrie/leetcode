# Initial thoughts
    # Probably similar to deep copy of linked list question
    # Iterate through graph once to extract nodes into some data structure
    # At the same time, keep hash that corresponds between original nodes and copies
    # Iterate through graph again to populate neighbors, but use copies in hash
    # Easier to do DFS because of some weird keyerror stuff
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copies = {}

        def dfs(node):
            if node in copies:
                return copies[node]
            copy = Node(node.val)
            copies[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        if node: return dfs(node)
        return None
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''