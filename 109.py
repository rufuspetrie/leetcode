# Initial thoughts
    # Similar to 108, just need fancier way of finding median
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Intended way: find median in LL by using fast and slow pointer
            # for each call of gen
        px = head
        vals = []
        while px:
            vals.append(px.val)
            px = px.next
        
        def gen(vals):
            if not vals: return None
            idx = len(vals)//2
            root = TreeNode(val = vals[idx])
            root.left = gen(vals[:idx])
            root.right = gen(vals[idx+1:])
            return root

        root = gen(vals)
        return root