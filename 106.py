# Initial thoughts
    # Very similar to 105
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder or not postorder: return None
        root = TreeNode()
        root.val = postorder[-1]
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        
        return root