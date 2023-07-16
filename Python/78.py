# Notes
    # Can visualize outputs generated as tree where each layer is a choice of
        # including/excluding a particular value
        # e.g. first layer is include/don't include 1, yieling [1] and []
        # second layer is include/don't include 2, yielding [1,2], [1], [2], []
        # continue this process for all elements
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subset = []
        def dfs(idx = 0):
            if idx >= len(nums):
                subsets.append(subset[:])
                return

            # Include element
            subset.append(nums[idx])
            dfs(idx + 1)

            # Do not include element
            subset.pop()
            dfs(idx + 1)

        dfs()
        return subsets