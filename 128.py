# First idea:
    # Heapify list, pop all elements, keep track of streaks where heappop = cur + 1
# Better solution:
    # change nums into a set
    # can check if elements are the start of a sequence by checking if (i-1) is in set
    # can check if successors are in the set in constant time
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for i in nums:
            if (i-1) not in nums:
                cur_len = 1
                while (i+1) in nums:
                    cur_len += 1
                    i += 1
                max_len = max(cur_len, max_len)

        return max_len