# Initial thoughts
    # Need node with degree n - 1 and no outgoing edges
    # Can just make trusts/trusted array
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust: return 1
        trusts = [0] * (n + 1)
        trusted = [0] * (n + 1)
        for i, j in trust:
            trusts[i] += 1
            trusted[j] += 1

        for i, v in enumerate(trusted):
            if v == (n - 1) and trusts[i] == 0:
                return i

        return -1