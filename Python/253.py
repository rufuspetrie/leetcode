# Initial thoughts
    # need to find the maximum number of overlapping intervals
    # sort intervals like 252
    # iterate until you find overlapping intervals
    # count the number of intervals that overlap with the first
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals = intervals.sort(key = lambda x: x[0])
        rooms = 1
        for i in range(1, len(intervals)):
            e1 = intervals[i-1][1]
            s2 = intervals[i][0]
            if e1 > s2:
                j = i
                overlaps = 0
                while j < len(intervals) and intervals[j][0] < e1:
                    overlaps += 1
                    j += 1
                rooms = max(rooms, overlaps + 1)

        return rooms