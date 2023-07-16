# Initial thoughts
    # Probably want to work index-by-index and convert each digit manually
    # Reversing the numbers might also make it easier
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0 for i in range(len(num1) + len(num2))]
        
        for x in range(len(num1)):
            for y in range(len(num2)):
                digit = (int(num1[x]) * int(num2[y]))
                res[x + y] += digit
                res[x + y + 1] += res[x + y] // 10
                res[x + y] %= 10

        res = res[::-1]
        idx = 0
        while idx < len(res) and res[idx] == 0: idx += 1
        return "".join(map(str, res[idx:]))