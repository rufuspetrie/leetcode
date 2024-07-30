/*
- Using prefix/postfix arrays eliminates most repetition
*/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefixes = {1};
        vector<int> postfixes = {1};
        for(int i = 0; i < nums.size(); i++){
            prefixes.push_back(nums[i] * prefixes[prefixes.size() - 1]);
        }
        for(int i = nums.size() - 1; i >= 0; i--){
            postfixes.push_back(nums[i] * postfixes[postfixes.size() - 1]);
        }
        reverse(postfixes.begin(), postfixes.end());
        vector<int> result(nums.size());
        for(int i = 0; i < nums.size(); i++){
            result[i] = prefixes[i] * postfixes[i + 1];
        }
        return result;
    }
};