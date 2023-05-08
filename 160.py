class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        a_nodes = {}
        a_nodes[headA] = 1
        px = headA
        while px.next:
            px = px.next
            a_nodes[px] = 1
        
        if headB in a_nodes.keys():
            return headB
        px = headB
        while px.next:
            px = px.next
            if px in a_nodes.keys():
                return px
        return None