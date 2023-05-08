# Notes
    # As usual, useful to make a dummy node before populating list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        pd = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                pd.next = ListNode(p1.val)
                pd = pd.next
                p1 = p1.next
            else:
                pd.next = ListNode(p2.val)
                pd = pd.next
                p2 = p2.next

        if p1: pd.next = p1
        if p2: pd.next = p2

        return dummy.next