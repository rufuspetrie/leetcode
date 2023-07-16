class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int: 
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i)
        if not ones:
            return 0
        
        gaps = []
        for i in range(len(ones) - 1):
            gaps.append(ones[i+1] - ones[i])
        
        res = 1
        for i in gaps:
            res *= i
        
        MOD = 10**9 + 7
        if not gaps:
            return 1
        return res % MOD