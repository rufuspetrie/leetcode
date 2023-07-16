# Why didn't I get this problem at first?
    # Brute force is silly
    # Next idea - do left/right maxes like the water fill problem
        # Index only approach not valid since water fills entire interval
    # This algorithm: greedily move smaller boundary
        # Note that there can be scenarios where we need to move the larger
            # boundary to get to an even larger boundary
        # However, this won't improve the filled area until we find a boundary
            # on the other side >= the old boundary we just moved from
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area