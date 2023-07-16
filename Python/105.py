# Initial thoughts
    # No clue on this one, should probably whiteboard it later
    # Preorder - process root, left subtree, right subtree
    # Inorder - process left subtree, root, right subtree
# Observation
    # Consider p = [3,9,20,15,7], i = [9,3,15,20,7]
    # We know that p[0] = 3 will be the root node
    # Everything before 3 in the inorder tree will be part of the left subtree
    # Everything after 3 in the inorder tree will be part of the right subtree
    # Because only one element comes before 3 in i, the left subtree only has a 9
    # Using this general pattern, split the i array into trees/subtrees depending
        # on the position of the root nodes from p
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root