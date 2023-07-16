# Top of the triangle is base case so can ignore
# Bottom/up solution is better than top/down because if we go bottom/up,
    # we know the cost of getting to each node
# Algorithm:
    # Start at 2nd to bottom row
    # Add minimum of the two lower values to find cost of reaching that node
    # Repeat until you reach the top of the triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        print(triangle)
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j:j+2])

        return min(triangle[0])