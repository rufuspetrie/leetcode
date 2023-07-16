class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None
        if left == right:
            return head
        
        px = head
        values = [px.val]
        while px.next:
            px = px.next
            values.append(px.val)

        values_rev = values[:left-1] + values[left-1:right][::-1] + values[right:]
        output = ListNode()
        px = output
        for i in range(len(values_rev)-1):
            px.val = values_rev[i]
            px.next = ListNode()
            px = px.next
        px.val = values_rev[-1]
        return output