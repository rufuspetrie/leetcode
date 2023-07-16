"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Algorithm: use bfs and set pointers equal to next in queue (None for last)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        queue = [root]
        while root:
            
            new_queue = []
            
            for i in queue: new_queue += [i.left, i.right]
            for i in range(len(new_queue)-1):
                new_queue[i].next = new_queue[i+1]
            new_queue[-1].next = None
            queue = new_queue
            
        return root