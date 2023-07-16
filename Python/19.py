# Thoughts
    # Original attempt was alright except for some edge case stuff
    # Need to be more careful thinking about edge cases
    # After you've got an algorithm that replicates a more concrete example,
        # think about how it will mess up if some dummy uses the algorithm
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(val = 0, next = head)
        slow = dummy
        fast = head
        for i in range(n): fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next