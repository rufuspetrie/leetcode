/*
- Encode: add strings into one string and either keep indices or delimeters
- Decode: go in opposite direction
*/
class Solution {
public:
    string encode(vector<string>& strs) {
        string result = "";
        for(int i = 0; i < strs.size(); i++){
            string str = strs[i];
            result += to_string(str.size()) + "#" + str;
        }
    }
    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while(i < s.size()){
            int j = i;
            while(s[j] != "#") j++;
            int length = stoi(s.substr(i, j - 1));
            string str = s.substr(j + 1, length);
            result.push_back(str);
            i = j + 1 + length;
        }
    }
    return result;
};