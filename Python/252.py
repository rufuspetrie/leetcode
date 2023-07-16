# Initial thoughts
    # Sort meeting according to start times
    # If an endtime ever surpasses the next start time, return False
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals = intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals)):
            e1 = intervals[i-1][1]
            s2 = intervals[i][0]
            if e1 > s2: return False
        
        return True