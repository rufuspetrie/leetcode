# Algorithm
    # Have a slow and fast pointer
    # If they meet, it's because the fast one looped and there's a cycle in the list
    # If not, there is no cycle
    # Note: condition on fast to avoid edge case headache
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True

        return False