class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        px = head
        while px and px.next != None:
            while px.next and px.val == px.next.val:
                px.next = px.next.next
            px = px.next

        return head