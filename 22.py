# Thoughts
    # Maybe keep two data structures simultaneously
        # String containing parenthese placed so far
        # Stack containing bottom parentheses
        # Need to also account for the number of open/closed parentheses used so far
        # Instead of keeping track of index with function argument, can keep track
            # of # of parentheses instead
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        stack = []
        max_len = 2*n

        def gen(open_n, closed_n):
            if len(stack) == max_len:
                combinations.append("".join(stack))
            else:
                if open_n < n:
                    stack.append("(")
                    gen(open_n + 1, closed_n)
                    stack.pop()
                if closed_n < open_n:
                    stack.append(")")
                    gen(open_n, closed_n + 1)
                    stack.pop()

        gen(0, 0)
        return combinations