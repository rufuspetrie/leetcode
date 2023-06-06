# Initial thoughts
    # Few cases:
        # precedes all intervals
        # falls in intervals, doesn't overlap
        # overlaps some interval(s)
        # comes after all intervals
# Easier way to think of it
    # Create a list and interate through the intervals
    # If the interval is behind the new one, add it to the res
    # If the interval is ahead of the new one, add new to res, return rest
    # If there's overlap, merge current intervals and continue the process
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), \
                max(intervals[i][1], newInterval[1])]

        res.append(newInterval)
        return res