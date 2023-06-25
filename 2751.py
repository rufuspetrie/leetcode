# Notes
    # Much easier to just generate an array of indexes and reference the arrays
        # than make a list of tuples
    # In particular, just modify the health in the original array after each collision
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idx = [i for i in range(n)]
        idx.sort(key = lambda x: positions[x])

        stack = []
        for i in idx:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack:
                    j = stack[-1]
                    if healths[i] == healths[j]:
                        healths[i] = 0
                        healths[j] = 0
                        stack.pop()
                        break
                    elif healths[i] > healths[j]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()
                    else:
                        healths[i] = 0
                        healths[j] -= 1
                        break
                    
        res = [h for h in healths if h]
        return res