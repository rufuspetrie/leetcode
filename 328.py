class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        ehead = head.next
        po = head
        pe = head.next
        while pe and pe.next:
            po.next = po.next.next
            po = po.next
            pe.next = pe.next.next
            pe = pe.next
        po.next = ehead
        return head