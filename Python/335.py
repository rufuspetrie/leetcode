# Note: we only need to consider the scenarios in which line 1 is crossed
    # because we can just rotate the grid and start over if it's fine
    # Line 4 crosses line 1
        # 3 < 1 and 4 > 2
    # Line 5 goes into line 1
        # 4 = 2 and 5 > (3 - 1)
    # Line 6 crosses line 1
        # 5 > (3 - 1) and 5 < (3) and 6 > (4 - 2) and 4 > 2
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        
        for i in range(len(distance)-3):
            
            # 4 crosses 1
            if distance[i+2] <= distance[i] and distance[i+3] >= distance[i+1]:
                return True

            # 5 goes into line 4
            if i < len(distance) - 4 and distance[i+1] == distance[i+3] and \
                distance[i+4] >= (distance[i+2] - distance[i]):
                return True

            # 6 crosses 1
            if i < len(distance) - 5 and distance[i+4] <= distance[i+2] \
                and distance[i+5] >= (distance[i+3] - distance[i+1]) \
                and distance[i+4] >= distance[i+2] - distance[i] \
                and distance[i+3] >= distance[i+1]:
                return True

        return False