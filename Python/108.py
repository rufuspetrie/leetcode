# Initial thoughts
    # At each step, make the root the median
    # Populate left/right subtrees using elements before/after median
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def gen_tree(nums):
            if not nums: return None
            mid = len(nums)//2
            root = TreeNode()
            root.val = nums[mid]
            root.left = gen_tree(nums[:mid])
            root.right = gen_tree(nums[mid+1:])
            return root

        return gen_tree(nums)