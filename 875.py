# Binary search explanation
    # Because this is a minimization problem,
        # we use binary search without an == condition
        # multiple rates can satisfy our constraints, but we want the smallest
    # Furthermore, we use a strict inequality for the binary search
        # so that we don't overshoot out desired value
    # For our increments, we use l = mid + 1 if it takes too long to eat
        # because we need to strictly increase the rate to finish eating
    # Also, we use r = mid when we finish eating because we don't know if
        # there are any smaller values of r that also satisfy our constraint,
        # so we need to make sure that our search interval keeps containing r
    # Note that this implementation of the algorithm will always terminate when
        # l reaches the optimal rate, which is why we fix r at mid and increment l
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        def time_to_eat(rate):
            return sum([ceil(i/rate) for i in piles])

        # Find smallest rate such that time_to_eat <= h
        while l < r:
            mid = (l + r)//2
            if time_to_eat(mid) > h:
                l = mid + 1
            else: # time_to_eat(mid) <= h
                r = mid

        return l