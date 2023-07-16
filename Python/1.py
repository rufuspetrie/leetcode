# Algorithm
    # Create hash storing index of each number
    # Iterate through nums and check whether target-num in hash
    # Observe that we don't have to store multiple indices because the first time
        # we encounter a pair we'll return the values
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, n in enumerate(nums):
            if target - n in index.keys():
                return [index[target - n], i]
            else:
                index[n] = i