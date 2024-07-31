/*
- If number, push to stack
- If operation, apply to top two numbers of stack
*/
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for(int i = 0; i < tokens.size(); i++){
            string token = tokens[i];
            if(token.size() > 1 || isdigit(token[0])){
                stk.push(stoi(token));
                continue;
            }
            int n2 = stk.top();
            stk.pop();
            int n1 = stk.top();
            stk.pop();

            int result = 0;
            if(token == "+") result = n1 + n2;
            else if(token == "-") result = n1 - n2;
            else if(token == "*") result = n1 * n2;
            else result = n1 / n2;
            stk.push(result);
        }
        return stk.top();
    }
};