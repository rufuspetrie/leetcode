# How does this problem work?
    # Recursive solution where leafs are the base case
    # Set a nonlocal variable res to keep track of the max diameter
    # We want to find the node with the highest combined left/right depth
    # At any given node, check the combined depth of the left/right subtree
    # After this, return 1 + max(left, rigth) to find the current node's
        # maximum depth and continue the algorithm a level higher
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res