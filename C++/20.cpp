/*
- As always, hash is good for character matching to reduce branches
- C++ stack implemenation has a top function instead of peek
- https://stackoverflow.com/questions/17032267/c11-range-based-for-loop-efficiency-const-auto-i-versus-auto-i
- Above link has good explanation of C++ auto looping
*/
class Solution {
public:
    bool isValid(string s) {
        stack<char> chars;
        unordered_map<char, char> matches = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };
        for(const auto& c: s){
            if(matches.find(c) != matches.end()){ // c in map, i.e. a closed bracket
                if(chars.empty()) return false;
                if(chars.top() != matches[c]) return false;
                chars.pop();
            }
            else{
                chars.push(c);
            }
        }
        return chars.empty();
    }
};