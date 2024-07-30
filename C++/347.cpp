/*
- Easy solution: sort counter or use heap
- Better solution: use bucket sort
    - As usual, set up a counter
    - Then, make a vector where each index contains a vector of elements that happen
    - that amount of times
*/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i++){
            map[nums[i]]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);
        for(auto it = map.begin(); it != map.end(); it++){
            buckets[it -> second].push_back(it -> first);
        }

        vector<int> result;
        for(int i = nums.size(); i >= 0; i--){
            if(result.size() >= k) break;
            if(!buckets[i].empty()){
                result.insert(result.end(), buckets[i].begin(), buckets[i].end());
            }
        }
        return result;
    }
};