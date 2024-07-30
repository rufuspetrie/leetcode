/*
- Easy way: use sorted version of string as key for hash
- Better way: use counter of string as hash key
*/
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(int i = 0; i < strs.size(); i++){
            string key = get_key(strs[i]);
            cout << key << endl;
            map[key].push_back(strs[i]);
        }
        vector<vector<string>> result;
        for(auto it = map.begin(); it != map.end(); it++){
            result.push_back(it -> second);
        }
        return result;
    }
private:
    string get_key(string str){
        vector<int> counter(26);
        for(int i = 0; i < str.size(); i++){
            counter[str[i] - 'a']++;
        }
        string key = "";
        for(int i = 0; i < counter.size(); i++){
            key.append(to_string(counter[i]) + "#");
        }
        return key;
    }
};