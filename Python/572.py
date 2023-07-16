# Initial thoughts
    # Make tree-equality function, apply recursively
# Major screw up
    # Need to make sure to call self.isSubtree for the recursive part of the final line
    # If we call the same_tree method there, it will recurse one time and then stop
    # If we call the isSubTree method instead, it will continually check for subtrees
        # that could be equal in all levels of the tree
class Solution:
    def same_tree(self, a, b):
        if not a and not b: return True
        if not a or not b: return False
        return a.val == b.val and self.same_tree(a.left, b.left) and self.same_tree(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot: return True
        if not root: return False
        if self.same_tree(root, subroot): return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)