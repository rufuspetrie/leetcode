class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int result = 0;
        stack<pair<int, int>> stk;
        for(int i = 0; i < heights.size(); i++){
            int idx = i;
            while(!stk.empty() && stk.top().second > heights[i]){
                int res = stk.top().second * (i - stk.top().first);
                idx = stk.top().first;
                result = max(res, result);
                stk.pop();
            }
            stk.push({idx, heights[i]});
        }
        while(!stk.empty()){
            int res = stk.top().second * (heights.size() - stk.top().first);
            result = max(res, result);
            stk.pop();
        }
        return result;
    }
};