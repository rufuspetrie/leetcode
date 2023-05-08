# Improved approach from editorial
# Previously, I found all subtrees and then serialized them
# This version is better because you can simultaneously track the nodes and serializations
# That way, you can tackle the problem in one part and not call the serialization function so much
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def search(node):
            if not node: return ""
            s = ("(" + search(node.left) + ")" + str(node.val) + "(" + search(node.right) + ")")
            if s not in d.keys(): d[s] = 1
            else: d[s] += 1
            if d[s] == 2: out.append(node)
            return s

        d = {}
        out = []
        search(root)
        return out