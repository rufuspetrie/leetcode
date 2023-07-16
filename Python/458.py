# Return the minimum number of pigs required to figure out which bucket was poisonous
# For one time period, there are 2^p configurations
# For t time periods, there are (1+t)^p configurations
# p = log(b)/log(1+t)
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1: return 0
        periods = minutesToTest // minutesToDie
        p = 1
        while (periods + 1) ** p < buckets:
            p += 1
        return p