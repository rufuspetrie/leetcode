# Initial thoughts
    # When robbing the houses in a circular arrangement, there are two possible outcomes
        # You do not rob the last house, in which case the maximum loot attainable will
            # be represted by the max of the regular array
        # You rob the last house, so you can not rob the first house - this means that
            # you can set the value of the first house to 0 and proceed as usual
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3: return max(nums)
        
        # When connected, can't rob the final house, so use len(nums) - 1
        loots = nums[:2]
        for i in range(2, len(nums) - 1):
            loots.append(max(nums[i] + max(loots[:i-1]), loots[i-1]))
        
        # In the case we rob the final house, can't rob the first, so make it 0
        nums_x = [0] + nums[1:]
        loots_x = nums_x[:2]
        for i in range(2, len(nums_x)):
            loots_x.append(max(nums_x[i] + max(loots_x[:i-1]), loots_x[i-1]))

        return max(loots_x + loots)