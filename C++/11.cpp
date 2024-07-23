/*
- Notice that greedy approach works better like the 2-sum solution
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int cur = 0;
        int out = 0;

        while(i < j){
            cur = (j - i) * min(height[i], height[j]);
            out = max(cur, out);
            if(height[i] <= height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return out;
    }
};