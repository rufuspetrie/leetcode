class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 or not root2:
            return root1 or root2

        base = TreeNode(val = root1.val + root2.val)
        base.left = self.mergeTrees(root1.left, root2.left)
        base.right = self.mergeTrees(root1.right, root2.right)

        return base