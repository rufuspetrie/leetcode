# Initial thoughts
    # If we interpret each row as a histogram, this becomes maximal rectangle
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if not stack: stack.append((i, h))
            ix = i
            while stack and h < stack[-1][1]:
                ix, hx = stack.pop()
                max_area = max(max_area, (i - ix) * hx)
            stack.append((ix, h))

        n = len(heights)
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (n - i) * h)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        nums = [0] * cols
        max_area = 0

        for row in matrix:
            for i, v in enumerate(row):
                if v == "1": nums[i] += 1
                else: nums[i] = 0
            max_area = max(max_area, self.largestRectangleArea(nums))
        
        return max_area