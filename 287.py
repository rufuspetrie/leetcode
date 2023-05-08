# Linked list cycle/Floyd's algorithm problem
    # The elements range from 1-n and there are n indices
    # If we consider each element value as the index it points to,
        # then eventually there will be a cycle when following pointers
    # Use Floyd's algorithm to find the start of this cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We're in the cycle when the slow and fast pointers meet
        n = len(nums)
        sp = nums[0]
        fp = nums[nums[0]]
        while sp != fp:
            sp = nums[sp]
            fp = nums[nums[fp]]

        # Run pointer from origin and internal point of cycle
        np = 0
        while np != sp:
            np = nums[np]
            sp = nums[sp]

        return np