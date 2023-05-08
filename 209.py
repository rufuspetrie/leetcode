# Initial thoughts
    # Maintain sliding window greater than sum
    # Compare lengths for each new window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        lp = 0
        rp = 0
        c_sum = nums[0]
        m_len = 10**5+1
        if c_sum >= target: m_len = 1
        while lp <= rp and rp < n - 1:
            rp += 1
            c_sum += nums[rp]
            while c_sum - nums[lp] >= target:
                c_sum -= nums[lp]
                lp += 1
            if c_sum >= target:
                m_len = min(rp - lp + 1, m_len)
        if m_len == 10**5+1: return 0
        return m_len