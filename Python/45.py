# Initial thoughts
    # can do BFS but it TLE's
    # for each jump, look ahead to the index with the highest index + jump value
    # jump there and increment counter accordingly
    # Note: code is much easier if you don't immediately set mj to nums[0]
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        steps = 0
        while r < len(nums) - 1:
            mj = 0
            for i in range(l, r + 1):
                mj = max(mj, nums[i] + i)
            l = r + 1
            r = mj
            steps += 1
        
        return steps