# Goal: count the number of valid arrays that end at each index
# Valid arrays will contain max_k/min_k, and no values greater/lesser
# Algorithm
    # Iterate through array
    # Keep track of last invald value
    # Keep track of last instance of min_k/max_k
    # If the invalid value is closer than the last min_k/max_k, no arrays end there
    # If the invalid value is earlier than the last min_k/max_k,
        # there will be min(min_k, max_k) - invalid arrays ending at index i
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Note: initialize last_inv to -1 so that arrays starting at index 0
            #  have length of at least 1
        last_minK = -1
        last_maxK = -1
        last_inv = -1
        count = 0

        # Note: must use all ifs because min_k can equal max_k
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                last_inv = i
            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i
            if min(last_minK, last_maxK) > last_inv:
                count += min(last_minK, last_maxK) - last_inv

        return count