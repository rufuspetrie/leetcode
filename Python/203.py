class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        values = [head.val]
        px = head
        while px.next:
            px = px.next
            values.append(px.val)

        values = [i for i in values if i != val]
        if len(values) == 0:
            return None
        output = ListNode(values[0])
        px = output
        for i in range(1, len(values)):
            px.next = ListNode(values[i])
            px = px.next
        return output