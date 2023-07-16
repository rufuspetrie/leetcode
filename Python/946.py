# Initial thoughts
    # Need to iterate through both arrays
    # Could do while pointer < len of both arrays
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        px = 0
        py = 0
        xs = []
        while px < len(pushed):
            xs.append(pushed[px])
            px += 1
            while xs and xs[-1] == popped[py]:
                xs.pop()
                py += 1

        return px == len(pushed) and py == len(popped)