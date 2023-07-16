# Initial thoughts
    # Probably easier to do iterative approach than find all overlapping intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []

        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
                intervals[i-1] = 0

        intervals = [i for i in intervals if i]
        return intervals