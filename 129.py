# DFS seems like best option
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.path_totals = 0
        def dfs(root, total = 0):
            if not root:
                return None
            total = 10 * total + root.val
            if not root.left and not root.right:
                self.path_totals += total
                return None
            dfs(root.left, total)
            dfs(root.right, total)

        dfs(root)
        return self.path_totals