# 0 <= n <= 10**9
# Solve this by finding digit contribution of each place
    # The one place contribues 1 every 10
        # Add n//10 * 10 + (n%10 != 0) (in cases like 151, check if a 1 remains)
    # The ten place contributes 10 every 100
        # Add n//100 * 10 + min(max(n%100 - 10, 0), 10)
            # e.g. 117 contributes 7 more 1's after doing //100
            # 117//100 - 10 = 7, add min of this or 10
            # the min protects against cases like 105 where 105//100 - 10 = -5
    # The 100 place contributes 100 every 1000
        # Add n//1000 * 100 + min(max(n%1000 - 100, 0), 100)
    # etc...
class Solution:
    def countDigitOne(self, n: int) -> int:
        base = 10
        total = 0
        while base <= n*10:
            total += (n//base) * (base/10) + min(max(n%base - base/10 + 1, 0), base/10)
            print(total)
            base *= 10
        return int(total)