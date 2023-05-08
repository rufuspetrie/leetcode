class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if head == None:
            return None
        hits = ""
        px = head
        while px.next:
            if px.val in nums:
                hits += "1"
            else:
                hits += "0"
            px = px.next
        if px.val in nums:
            hits += "1"
        else:
            hits += "0"
        hits = hits.split("0")
        hits = [i for i in hits if i != ""]
        return(len(hits))