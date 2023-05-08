# Note
    # The reason why your non-cheesey solution was slow before is because the lists
        # are roughly the same size
    # When merging sorted lists and repeatedly merging them into one list, you have to compare
        # relatively many elements with relatively few
    # It's a better policy to merge lists like you would in mergesort to minimize the amount of
        # comparisons you have to do when evaluating each list (think of the merge trees)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None

        # Merge helper function
        def merge(l1, l2):
            dummy = ListNode(0)
            p1 = l1
            p2 = l2
            p3 = dummy
            while p1 and p2:
                if p1.val < p2.val:
                    p3.next = ListNode(p1.val)
                    p1, p3 = p1.next, p3.next
                else:
                    p3.next = ListNode(p2.val)
                    p2, p3 = p2.next, p3.next
            if p1: p3.next = p1
            if p2: p3.next = p2
            return dummy.next
        
        # Merge pairs of lists instead of all lists with first element
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        
        return lists[0]