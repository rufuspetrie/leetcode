class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        first = [int(str(i)[0]) for i in nums]
        lasts = [i%10 for i in nums]
        count = 0
        
        for i in range(len(first) - 1):
            for j in range(i + 1, len(lasts)):
                if math.gcd(first[i], lasts[j]) == 1:
                    count += 1
                    
        return count