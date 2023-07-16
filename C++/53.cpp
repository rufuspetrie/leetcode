class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        int max = INT_MIN;
        for(int i = 0; i < n; i++){
            res += nums[i];
            if (res > max) max = res;
            if (res < 0) res = 0;
        }
        return max;
    }
};