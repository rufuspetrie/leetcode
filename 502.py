# Maximize profits from performing k jobs with w initial capital
# Note: your capital base does not deplete while completing projects,
# i.e. it's only a starting requirement and not a cost
# array gets 32/35, need to use heap

# Heap algorithm
# Sort (profits, capital) by capital ascending
# While capital is less than k, pop from array and push the profit onto the heap

# k = # projects
# w = initial capital
# profits = profit of each project
# capital = capital required to start project

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # Generate tuples of (profit, capital) sorted by capital requirement
        projects = [(profits[i], capital[i]) for i in range(len(profits))]
        projects = sorted(projects, key = lambda x: x[1])

        # Add projects below current capital to heap
        # Note: need to use negative profit to keep track of maximum instead of minimum
        pq = []
        k = min(k, len(profits))
        while k > 0:
            while projects and projects[0][1] <= w:
                heappush(pq, -1 * projects.pop(0)[0])
            if not pq:
                return w
            w += -1 * heappop(pq)
            k -= 1
        return w