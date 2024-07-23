/*
- As usual for hard array problems, think of it index by index
- Water contained at each index equals the minimum of it's left/right maxes minus its height
- Remember to take advantage of max/min function to avoid conditional branching
*/
class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left_maxes = {0};
        vector<int> right_maxes = {0};

        int cur = 0;
        int lm = 0;
        for(int i = 1; i < height.size(); i++){
            cur = height[i - 1];
            lm = max(cur, lm);
            left_maxes.push_back(lm);
        }

        cur = 0;
        int rm = 0;
        for(int i = height.size() - 2; i >= 0; i--){
            cur = height[i + 1];
            rm = max(cur, rm);
            right_maxes.push_back(rm);
        }
        reverse(right_maxes.begin(), right_maxes.end());

        int total = 0;
        for(int i = 0; i < height.size(); i++){
            total += max(0, min(left_maxes[i], right_maxes[i]) - height[i]);
        }
        return total;
    }
};