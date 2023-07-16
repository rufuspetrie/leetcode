# Algorithm
    # While neither list is empty, add the digit, find the carry
# Notes
    # while p1 or p2 or carry made this a lot easier because didn't have to worry about remainders
    # the oneline if/else statements are very useful for updating pointers when they might not exist
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        p1 = l1
        p2 = l2
        p3 = output
        carry = 0
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            digit = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            p3.next = ListNode(digit)
            p3 = p3.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return output.next