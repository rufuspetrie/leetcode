/*
- Hint: you can always use multiple data structures to make more functional ones
- Notice that simply tracking a minimum doesn't work because once the current min is popped you can't recall priors
- In particular, can use a regular stack for most functions and a monotonic stack for the minimum-tracking
*/
class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        if(min_stk.empty() || val < min_stk.top().first){
            min_stk.push({val, 1});
        }
        else if(val == min_stk.top().first){
            min_stk.top().second++;
        }
    }
    
    void pop() {
        if(stk.top() == min_stk.top().first){
            min_stk.top().second--;
        }
        if(min_stk.top().second == 0){
            min_stk.pop();
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stk.top().first;
    }
private:
    stack<int> stk;
    stack<pair<int, int>> min_stk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */