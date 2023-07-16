class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, n = 0):
            if not root:
                return None
            elif not root.left and not root.right and n + root.val == targetSum:
                return True
            else:
                n += root.val
                return dfs(root.left, n) or dfs(root.right, n)

        return dfs(root)