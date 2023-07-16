class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        vals = []

        def search(root):
            if not root: return None
            if root.left: search(root.left)
            if root.right: search(root.right)
            vals.append(root.val)

        search(root)
        return vals