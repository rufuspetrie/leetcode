class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def equal_trees(p, q):
            if p == None and q == None: return True
            if p == None or q == None: return False
            return p.val == q.val and equal_trees(p.left, q.right) and equal_trees(p.right, q.left)

        p = root.left
        q = root.right

        return equal_trees(p, q)