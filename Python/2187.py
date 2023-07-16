# Binary search
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = totalTrips * min(time)

        while l < r:
            mid = (l + r)//2
            trips = sum([mid//i for i in time])
            if trips >= totalTrips:
                r = mid
            else:
                l = mid + 1

        return l