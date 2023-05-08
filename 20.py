# Mental Note
    # whenever using conditional with a bunch of pair equality checks like this,
        # making a hash will let you write one line instead
class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                if len(stack) == 0: return False
                elif c in d.keys() and stack[-1] == d[c]: stack.pop()
                else: stack.append(c)

        return len(stack) == 0