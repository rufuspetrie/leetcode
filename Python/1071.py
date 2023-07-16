# Observation: if str1 and str2 are both multiples of one string,
# then str1 + str2 =  str2 + str1, the gcd string will be gcd of the string lengths
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd
        if str1+str2 != str2 + str1:
            return ""
        else:
            return str1[:gcd(len(str1), len(str2))]