# Initial thoughts
    # Each time you take an element from the end of the list, the next element you need from
        # the end becomes the final element of the list
    # Therefore, the problem becomes placing the current final node in the list
        # between each pair of elements in the list
    # How can we make a loop to do this? When does this process terminate?
        # It seems to end when there are not a next, nextnext in the list
# Problem
    # This first approach TLE'd on some bullshit leetcode edge input
    # Looking at it again, it appears that you can also get the answer from splicing together
        # the first half of the list (ascending) with the reversed second half of the list
    # Anyways, in the future be sure to try and notice all the patterns in the question
        # instead of just jumping at the first mechanism you see to produce the answer
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find middle element of the list
        if not head: return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge lists
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2