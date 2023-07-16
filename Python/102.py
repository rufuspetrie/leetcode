# Initial thoughts
    # Use BFS, process one level at a time
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        result = []
        queue = [root]
        while queue:
            new_queue = []
            vals = []
            for i in queue:
                vals.append(i.val)
                if i.left: new_queue.append(i.left)
                if i.right: new_queue.append(i.right)
            result.append(vals)
            queue = new_queue

        return result