# Initial thoughts
    # add max/min to function to search subtrees
    # check child validity and recurse
# Clarification
    # This is actually a fairly succinct way of writing the code
    # For the left subtree, we only update the maximum value
    # For the right subtree, only update the minimum value
    # This way, we can only include one expression comparing the values
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, min_val = -float("inf"), max_val = float("inf")):
            if not root: return True
            if root.val <= min_val or root.val >= max_val: return False
            return valid(root.left, min_val, root.val) and valid(root.right, root.val, max_val)

        return valid(root)