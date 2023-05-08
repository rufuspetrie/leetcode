# Ideas
    # Like other array problems, might be easier to consider individual indices
    # Observation: once there's a smaller element in the stack, the height
        # of an element can no longer be used to form rectangles
    # Want to keep monotonic stack, but not sure how to handle cases like adding
        # the middle rectangle in example 1
# Part I tripped up on
    # When adding a new element to the stack, the rectangle made up by the smaller
        # element extends farther backwards than its index
    # Therefore, when popping old elements, the index  of the new element will
        # be the index of the final element that you pop from the stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        # Add areas found when popping elements
        for i, h in enumerate(heights):
            if not stack: stack.append((i, h))
            ix = i
            while stack and h < stack[-1][1]:
                ix, hx = stack[-1]
                max_area = max(max_area, (i - ix) * hx)
                stack.pop()
            stack.append((ix, h))

        # Add areas from final stack
        n = len(heights)
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (n - i) * h)

        return max_area