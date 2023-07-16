# Initial thought
    # Make DFS to find maximum path sum starting at node
    # Starting from node, add subtrees if their sum is greater than 0
# Note
    # For any given path, you can only include both the right/left subtrees of the root node
        # i.e. you can't split the path because to traverse it you'd need to backtrack
        # An example of this would be [5,4,8,11,null,13,4,7,2,null,null,null,1]
    # Therefore, instead of finding subtrees with maximum sums,
        # need to find subtree with maximum pathsum without traveling down right AND left paths
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def dfs(root):
            if not root: return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # Maximum value with a split
            result[0] = max(result[0], root.val + left + right)
            
            # Maximum value without a split
            return root.val + max(left, right)

        dfs(root)
        return result[0]