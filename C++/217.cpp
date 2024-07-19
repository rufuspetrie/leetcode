class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> nums_map;
        for(int i = 0; i < nums.size(); i++){
            if(nums_map[nums[i]] == 1) return true;
            nums_map[nums[i]]++;
        }
        return false;
    }
};