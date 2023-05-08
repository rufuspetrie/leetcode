# Thoughts
    # Want to use dummy node to work on first group, but not sure how this will work out
        # when modifying k-groups beyond the first
    # Could possibly just maintain a prev pointer and update when finished with groups
    # Overall, this problem amounts to making the usual dummy pointer to start reversing groups,
        # finding the node to stop swapping at, and letting the previous node be the next dummy
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_dummy = dummy

        while True:
            k_node = self.get_k(prev_dummy, k)
            if not k_node: break
            next_group = k_node.next

            prev = k_node.next
            cur = prev_dummy.next

            # Reverse current group of nodes
            while cur != next_group:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            temp = prev_dummy.next
            prev_dummy.next = k_node
            prev_dummy = temp

        return dummy.next

    # Function to skip ahead k nodes
    def get_k(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur