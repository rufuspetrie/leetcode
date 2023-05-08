class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        values = [head]
        px = head
        while px.next != None:
            px = px.next
            values.append(px)
        return values[len(values)//2]