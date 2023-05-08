# Note
    # Should probably just try to do this using reservoir sampling at some point
from random import randint
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.len = 0
        px = head
        while px:
            self.len += 1
            px = px.next

    def getRandom(self) -> int:
        r = randint(0, self.len-1)
        px = self.head
        for i in range(r):
            px = px.next
        return px.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()