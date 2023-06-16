# Initial thoughts
    # Not sure how DP/optimal substructure will work for this one
# Algorithm
    # Can't consider sequences to pop because there's too many possibilities
    # Instead, fix pivots and wait to pop the pivot until last
    # This way, you can treat the remaining left/right subarrays to be
        # popped that don't depend on the other side
# Note: this is actually the same as the matrix multiplication DP problem
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        DP = {}
        nums = [1] + nums + [1]

        for o in range(2, len(nums)):
            for l in range(len(nums) - o):
                r = l + o
                for m in range(l + 1, r):
                    c = nums[l] * nums[m] * nums[r]
                    c += DP.get((l, m), 0) + DP.get((m, r), 0)
                    DP[(l, r)] = max(c, DP.get((l, r), 0))

        return DP.get((0, len(nums) - 1), 0)