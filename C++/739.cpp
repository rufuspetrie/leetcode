/*
- Use monotonic stack and keep track of indices
*/
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        vector<int> result(temperatures.size());

        for(int i = 0; i < temperatures.size(); i++){
            int time = i;
            int temp = temperatures[i];
            while(!stk.empty() && stk.top().second < temp){
                result[stk.top().first] = time - stk.top().first;
                stk.pop();
            }
            stk.push({time, temp});
        }
        return result;
    }
};