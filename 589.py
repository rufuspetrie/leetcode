"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        vals = []

        def search(root):
            if not root: return None
            vals.append(root.val)
            for i in root.children: search(i)

        search(root)
        return vals