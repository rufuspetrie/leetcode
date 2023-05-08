# Initial thoughts
    # Do DFS and keep track of maximum value observed
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return None
        good_count = 0

        def dfs(root, cur_max = float("-inf")):
            if root:
                nonlocal good_count
                if root.val >= cur_max:
                    cur_max = root.val
                    good_count += 1
                dfs(root.left, cur_max)
                dfs(root.right, cur_max)

        dfs(root)
        return good_count