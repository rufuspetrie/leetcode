# Initial thoughts
    # Other way of phrasing - can we pick subset that equals sum(A)//2
    # Brute force - generate all subsets and compare sums - not feasible
    # This feels similar to LIS except we check sum instead of increasing
# Algorithm
    # Use set
    # Iterate through nums
        # Add nums[i] + s for each s in the set
    # Note: can't update a set while using it as an interable
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        DP = set()
        DP.add(0)
        t = sum(nums)//2
        for i in nums:
            DP2 = set()
            for j in DP:
                DP2.add(j)
                DP2.add(i+j)
            DP = DP2

        print(DP)
        return t in DP