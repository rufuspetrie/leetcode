# Algorithm
    # For each index in the array, swap with the first index
    # Recursively call on the right subarray until there's only one element
        # left, in which case add the permutations to the list
    # Unswap after the recursive call to backtrack
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(idx = 0):
            if idx == n:
                result.append(nums[:])
            else:
                for i in range(idx, n):
                    nums[idx], nums[i] = nums[i], nums[idx]
                    dfs(idx + 1)
                    nums[idx], nums[i] = nums[i], nums[idx]

        dfs()
        return result