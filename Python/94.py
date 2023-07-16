# Notes
    # Inorder traversals go in the sequence leftchild, parent, rightchild
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def search(root):
            if not root: return None
            if root.left: search(root.left)
            vals.append(root.val)
            if root.right: search(root.right)

        search(root)
        return vals