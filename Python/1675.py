# Can divide even numbers by 2
# Can multiply odd numbers by 2

# The maximum deviation will always be max - min
# Even numbers' initial values are their maximum
# Odd numbers' initial values are their minimum

# First approach: multiple min elements until even min, divine max elements until odd max
# This fails for [3,5] because they're both odd, so changing one to even can make different smaller
# New strategy: convert all numbers to even while loading into heap, then keep track of max dif manually

import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        mn = 10**9
        
        for i in nums:
            if i % 2 == 0:
                heappush(pq, -i)
                mn = min(mn, i)
            else:
                heappush(pq, -2*i)
                mn = min(mn, 2*i)

        dif = -pq[0] - mn
        while pq[0] % 2 == 0:
            mx = -heappop(pq)
            dif = min(dif, mx - mn)
            heappush(pq, -mx//2)
            mn = min(mn, mx//2)

        return min(-pq[0] - mn, dif)