/*
- Unique elements - no need to sort the vector
- Steps
    - Keep a vector of current subset
    - For each element in the array, perform DFS both including/excluding the element
*/
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> cur;
        dfs(nums, 0, cur, result);
        return result;
    }
private:
    void dfs(vector<int>& nums, int start, vector<int>& cur, vector<vector<int>>& result){
        result.push_back(cur);
        for(int i = start; i < nums.size(); i++){
            cur.push_back(nums[i]);
            dfs(nums, i + 1, cur, result);
            cur.pop_back();
        }
    }
};