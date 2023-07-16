# Initial thoughts
    # Base case: no root, return zero
    # If there are children, return 1 + max depth of the subtrees
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))