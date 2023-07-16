# Initial thought
    # Do level order traversal with BFS, return only final nodes in the layer
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        result = []
        queue = [root]
        while queue:
            vals = []
            new_queue = []
            for i in queue:
                vals.append(i.val)
                if i.left: new_queue.append(i.left)
                if i.right: new_queue.append(i.right)
            result.append(vals[-1])
            queue = new_queue

        return result