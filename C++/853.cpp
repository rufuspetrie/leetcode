/*
- Can make this a bit easier by constructing ETA's in initial array
*/
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> arr;
        for(int i = 0; i < position.size(); i++){
            arr.push_back({position[i], speed[i]});
        }
        sort(arr.begin(), arr.end());
        reverse(arr.begin(), arr.end());

        stack<double> stk;
        for(int i = 0; i < arr.size(); i++){
            double ETA = (double) (target - arr[i].first) / arr[i].second;
            if(stk.empty() || ETA > stk.top()) stk.push(ETA);
        }
        
        return stk.size();
    }
};