# Initial thoughts
    # LCA - DEEPEST (not lowest value) node that has p and q as descendents
    # Three cases
        # root < p and q - root is in the right subtree
        # root > p and q - root is in the left subtree
        # p < root < q - root is the LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: return root