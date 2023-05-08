# Note:
    # Can keep min in a separate stack and only push to that stack if element < min
    # When popping elements, need to check if pop'd element is also top of min_stack
    # This works because for any element greater than the min, it must be popped before
        # the min, so there will always be a smaller element than it in the stack
    # This is an example of a monotonic stack
class MinStack:

    def __init__(self):
        self.x = []
        self.min_x = []

    def push(self, val: int) -> None:
        self.x.append(val)
        if not self.min_x or val <= self.min_x[-1]: self.min_x.append(val)

    def pop(self) -> None:
        if self.x:
            if self.x[-1] == self.min_x[-1]:
                self.min_x.pop()
            self.x.pop()

    def top(self) -> int:
        if self.x: return self.x[-1]

    def getMin(self) -> int:
        if self.min_x: return self.min_x[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()