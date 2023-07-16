# Sieve of Eratosthenes (easier approach than before)
    # Generate sieve array then a prime array
    # Start at 3 instead of 2
        # When constructing sieve array, we can just start at 3, increment by 2
    # When skipping evens, can let p**2 be the first prime eliminated
        # all factors lower than p will have already been eliminated
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        p = 3
        sieve = [1 for _ in range(n+1)]

        while p**2 <= n:
            if sieve[p]:
                for i in range(p**2, n+1, p):
                    sieve[i] = 0
            p += 2
        
        res = [2]
        for i in range(3, n+1, 2):
            if sieve[i]:
                res.append(i)

        if res[-1] == n: return len(res) - 1
        return len(res)