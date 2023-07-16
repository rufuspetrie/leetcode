# Algorithm
    # Use stack to keep track of temperatures and indices
    # While the newest element is greater than the top of the stack,
        # pop the top and find wait times by subtracting the indices
    # Otherwise, push elements to the stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        waits = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx = stack.pop()[0]
                waits[idx] = i - idx
            stack.append((i, t))

        return waits