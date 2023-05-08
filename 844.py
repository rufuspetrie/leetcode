class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def decode(self, s):    
            stack = []
            for i in range(len(s)):
                if s[i] != "#": stack.append(s[i])
                else: 
                    if len(stack) > 0:
                        stack.pop()
            return "".join(stack)

        return decode(self, s) == decode(self, t)