/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int result = 0;
        dfs(root, result);
        return result;
    }
private:
    int dfs(TreeNode* root, int& result){
        if(root == NULL) return 0;
        int left = dfs(root -> left, result);
        int right = dfs(root -> right, result);
        result = max(result, left + right);
        return 1 + max(left, right);
    }
};
/*
- Idea - keep a result variable
    - for each node, recursively calculate the depth of each subtree
    - update result if the sum of the subtrees is greater than the current maximum
*/