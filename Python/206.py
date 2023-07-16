# Note: need to condition on cur instead of cur.next because if you use cur.next,
    # you will not reverse the pointer for the final node
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev