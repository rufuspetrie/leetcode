# Initial thoughts
    # Probably relates to inorder traversal
    # Can just make array of the values with inorder, but this will be slow-ish
    # Can keep rank variable and increment each time we reach the far left node
    # This way being annoying for some reason, but a stack approach also works
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        stack = []
        cur = root
        rank = 0

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            rank += 1
            if rank == k: return cur.val
            cur = cur.right