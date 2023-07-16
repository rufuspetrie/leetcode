# Algorithm:
    # Use stack to keep track of parenthese while iterating through s
    # Instead of storing parentheses values, store the indexes
        # this is a lot cleaner than storing pointers and cur_len variables
        # similar to index/value storage in monotonic stack problems
    # In particular, keep only left parenthesis indexes in the stack
    # If you encounter right parenthese, pop the stack
        # If the stack is empty, it's the end of the valid substring
        # Add the current ")" index to the stack to signify the start of a new string
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m_len = 0
        stack = [-1]
        for i, p in enumerate(s):
            if p == "(": 
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                m_len = max(m_len, i - stack[-1])

        return m_len