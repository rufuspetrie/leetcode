class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        vals = []

        def dfs(root):
            if not root:
                return None
            vals.append(root.val)
            if root.left: vals.append(dfs(root.left))
            if root.right: vals.append(dfs(root.right))

        dfs(root)
        vals = [i for i in vals if i != None]
        for i in vals:
            for j in vals:
                if i + j == k and i != j:
                    return True
        return False