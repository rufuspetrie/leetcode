# Initial thoughts
    # Use BFS to explore tree layer by layer
    # Alternate appending normal/reverse values layer by layer
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None

        values = []
        sign = 1
        queue = [root]
        new_nodes = []

        while queue:
            # Extract values from queued objects, flip sign to zigzag
            if sign:
                values.append([i.val for i in queue])
            else:
                values.append([i.val for i in queue][::-1])
            sign ^= 1

            # Update queue of nodes to explore
            for i in queue:
                if i.left: new_nodes.append(i.left)
                if i.right: new_nodes.append(i.right)
            queue = new_nodes
            new_nodes = []

        return values