# Initial thoughts
    # Can probably do something like Floyd's algorithm to avoid hashing,
        # but we hate Floyd
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 1: return 1
            if n in visited: return 0
            visited.add(n)