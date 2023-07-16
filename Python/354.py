# Initial thoughts
    # Can sort envelopes by length/width
    # Problem then becomes LIS
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        nums = [i[1] for i in envelopes]
        DP = []
        for i in nums:
            if not DP or DP[-1] < i:
                DP.append(i)
            else:
                idx = bisect_left(DP, i)
                DP[idx] = i
        
        return len(DP)