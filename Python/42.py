# Notes
    # This seems like the valid subarray problem where it's likely easier to generate solution
        # index by index instead of trying to find a solution using subarrays
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1: return 0
        
        # Generate left maxes
        left_maxes = [0]
        for i in range(len(height) - 1):
            if height[i] > left_maxes[-1]:
                left_maxes.append(height[i])
            else:
                left_maxes.append(left_maxes[-1])

        # Generate right maxes
        right_maxes = [0]
        for i in range(len(height) - 1, 0, -1):
            if height[i] > right_maxes[-1]:
                right_maxes.append(height[i])
            else:
                right_maxes.append(right_maxes[-1])
        right_maxes = right_maxes[::-1]

        # At each index, return the minimum of the left/right maxes minus the current height
        total = 0
        for i, h in enumerate(height):
            if right_maxes[i] and left_maxes[i]:
                total += max(0, min(left_maxes[i], right_maxes[i]) - height[i])
        return total