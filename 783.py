class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def extract_values(root):
            output = []
            if root:
                output = extract_values(root.left)
                output.append(root.val)
                output += extract_values(root.right)
            return output

        output = extract_values(root)
        output = sorted(output)
        difs = []
        for i in range(len(output) - 1):
            difs.append(output[i+1] - output[i])
        return min(difs)