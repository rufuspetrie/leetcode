# Mininum number of steps to reach node ==> BFS might work
# Algorithm
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        target = len(arr) - 1
        if len(arr) < 2:
            return 0

        # Dictionary of element indices
        d = {}
        for i in range(len(arr)):
            if arr[i] not in d.keys():
                d[arr[i]] = [i]
            else:
                d[arr[i]].append(i)

        # Note: d[arr[i]].clear() prevents us from iterating through sets of indices
        #   multiple times
        explored = set()
        steps = 0
        queue = [0]
        while queue:
            steps += 1
            new_queue = []
            for i in queue:
                explored.add(i)
                if (i-1) > 0 and (i-1) not in explored:
                    new_queue.append(i-1)
                if (i+1) < len(arr) and (i+1) not in explored:
                    new_queue.append(i+1)
                for i in d[arr[i]]:
                    if i not in explored:
                        new_queue.append(i)
                d[arr[i]].clear()
            if target in new_queue:
                return steps
            queue = new_queue
            new_queue = []

        return False     