# Observations
    # When generating the permutations, the first permutation is always strictly increasing,
        # and the last permutation is always strictly decreasing
        # e.g. 123 ==> 321
    # We generate permutations in order by fixing a prefix and generating
        # permutations for the resulting subarray
    # The prefixes that come before a subarray always appear in increasing order
    # When we exhaust the permutations for a subsequence (it monotonically decreases),
        # the prefix becomes part of the subsequence,
        # and the next larger element becomes the prefix
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        # Find first nondecreasing element at end of the array
        if len(nums) < 2: return nums
        idx = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                idx = i - 1
                break
        
        # No nondecreasing element - last permutation
        if idx == -1: 
            nums[:] = nums[::-1]
            return

        # Find first element greater than nums[idx]
        idy = None
        for i in range(len(nums)-1, idx, -1):
            if nums[i] > nums[idx]:
                idy = i
                break

        # Flip idx and idy
        nums[idx], nums[idy] = nums[idy], nums[idx]

        # Reverse rest of the array if necessary
        if idx < len(nums) - 2:
            nums[idx+1:] = nums[idx+1:][::-1]