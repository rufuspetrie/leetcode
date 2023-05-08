# Initial thoughts
    # Can just keep pointers in visited, check new elements
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return None
        px = head
        visited = [head]
        while px.next != None:
            px = px.next
            if px in visited:
                return px
            else:
                visited.append(px)
        return None