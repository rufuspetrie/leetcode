# Initial thoughts
    # Recursive solution ==> roots are equal, p.r = q.r, p.l = q.l
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) \
        and self.isSameTree(p.right, q.right)