/*
- Can use hash set
- In particular, check if (n-1) isn't in hash (number begins a sequence),
- then check for consecutive numbers also using the hash
*/
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int output = 0;
        for(auto &n: s){
            if(!s.count(n - 1)){
                int length = 1;
                while(s.count(n + length)) ++length;
                output = max(output, length);
            }
        }
        return output;
    }
};