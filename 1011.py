# DP solution is too slow so need to use binary search
# That is, enumerate possible weight capacities and find minimum via search
# Lower limit: max(weights) (minimum weight needed to fit largest package)
# Upper limit: sum(weights) (this allows you to send all packages in one day)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # Function to determine whether you can load x weights in y days with z capacity
        def valid(weights, days, capacity):
            time = 1
            load = 0
            for i in weights:
                if i + load > capacity:
                    time += 1
                    load = 0
                load += i
            return time <= days

        l = max(weights)
        r = sum(weights)
        minimum = l
        while l <= r:
            mid = (l+r)//2
            if valid(weights, days, mid):
                minimum = mid
                r = mid - 1
            else:
                l = mid + 1

        return minimum