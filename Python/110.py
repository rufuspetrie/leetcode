# Initial thoughts
    # A height-balanced binary tree is a binary tree in which the depth of the 
        # two subtrees of every node never differs by more than one
    # Note: just compiling leaf depths or first-null-depths will not work for
        # this because of test cases like [1,2,3,4,5,6,null,8]
    # Proper idea: check for equality between depths of left/right subtree
        # and recursively apply to the subtrees
# Improved algorithm
    # To avoid dfs recalculations, build solution by bottom up by finding
        # height from 1 + max(l, r) instead of doing DFS at each node
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balance = abs(left[1] - right[1]) <= 1 \
            and left[0] and right[0]
            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]