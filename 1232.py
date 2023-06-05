# Initial thoughts
    # Easy to make helper function for computing slopes
    # Easy to compute one slope then check the rest for parity than compute y coords
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2: return True
        c = coordinates

        def slope(a,b):
            if a[0] != b[0]:
                return (b[1] - a[1]) / (b[0] - a[0])
            else:
                return "DNE"

        s = slope(c[0], c[1])
        for i in range(1, len(c) - 1):
            if slope(c[i], c[i + 1]) != s:
                return False

        return True