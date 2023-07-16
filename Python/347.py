# Original approach: use counter and sort items
    # this is easy but unnecessary b/c we only need the first k more frequent elements
# Second approach: use heap
    # cba'd implementing because heapq is annoying with alternate keys
# Best approach: bucket sort
    # Create array where the index equals the count,
        # and the values are the elements having that particular count
    # Using this array, can just iterate backwards until we observe k elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        bucket = [[] for i in range(n+1)]

        # Populate bucket
        for i in c.items():
            element, count = i
            bucket[count].append(element)

        # Iterate backwards through bucket and add k elements
        output = []
        idx = n
        while len(output) < k:
            if bucket[idx]: output.extend(bucket[idx])
            idx -= 1

        return output