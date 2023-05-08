# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        idx = 50
        while idx > 40:
            idx = (rand7()-1)*7 + rand7()
        return 1 + (idx - 1) % 10