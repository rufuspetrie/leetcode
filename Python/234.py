class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return None
        px = head
        values = []
        while px.next != None:
            values.append(px.val)
            px = px.next
        values.append(px.val)
        return values == values[::-1]