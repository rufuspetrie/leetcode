/*
- Use the fact that xXORx = 0
- In particular, XOR 0 by each number in the array and then each number 1-N
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            result ^= nums[i];
        }
        for(int i = 0; i < nums.size() + 1; i++){
            result ^= i;
        }
        return result;
    }
};