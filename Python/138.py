"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Initial thoughts
    # Can just iterate through the linked list to make copies of the values
    # Can't do a single iteration to make the random variable because that node
        # may not exist yet
    # Can't iterate twice because the next/random pointers may be behind the current node
    # Therefore, probably want to use some type of hash to store nodes so that you
        # can instantly find the linked one when populating the copy
# Algorithm
    # Iterate through the linked list and create nodes containing the same value for each pointer
    # Iterate through the list again
        # Set the mapped node's next value to the map of the old.next value
        # Set the mapped node's random value to the map of the old.random value
    # Need to include {None: None} in the hash for nodes with null pointers
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_nodes = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            old_nodes[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old_nodes[cur]
            copy.next = old_nodes[cur.next]
            copy.random = old_nodes[cur.random]
            cur = cur.next

        return old_nodes[head]