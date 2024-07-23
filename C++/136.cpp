/*
- Any number XOR'd with itself will equal zero
- Therefore, to find the unique number, can take XOR product of entire array
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            result ^= nums[i];
        }
        return result;
    }
};