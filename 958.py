# Use BFS
# from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return true
        queue = [root]
        
        # Any none's must be final layer, to right of all values
        while queue:
            new_queue = []
            for i in queue:
                if i:
                    new_queue.append(i.left)
                    new_queue.append(i.right)

            # Are there any Nones
            nones = False
            for i in new_queue:
                if not i: nones = True
            
            # If any Nones, check if it's the final layer
            final = True
            for i in new_queue:
                if i and (i.right or i.left):
                    final = False

            # If nones and not final, return false
            if nones and not final: 
                return False

            # If nones and final, check that they're all the way right
            if nones and final:
                none_idx = -1
                for i in range(len(new_queue)):
                    if not new_queue[i]:
                        none_idx = i
                        break
                if none_idx < len(new_queue) - 1:
                    print(none_idx)
                    for i in range(none_idx + 1, len(new_queue)):
                        if new_queue[i]:
                            return False

            queue = new_queue

        return True