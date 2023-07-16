class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        
        def search(root):
            if not root:
                return None
            vals.append(root.val)
            if root.left: search(root.left)
            if root.right: search(root.right)

        search(root)
        return vals