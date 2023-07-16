# Initial thoughts
    # When intervals overlap, how do you know which one to prune? Longer?
    # Greedy solution ==> remove interval that ends later (lower chance of overlap)
    # Note: easier to just keep track of end values than index both start/end
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        total = 0
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                last_end = min(last_end, end)
                total += 1

        return total