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
        if(min_stk.empty() || val < min_stk.top()){
            min_stk.push(val);
        }
        else if(val == min_stk.top()){
            min_stk.push(val);
        }
    }
    
    void pop() {
        if(stk.top() == min_stk.top()){
            min_stk.pop();
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stk.top();
    }
private:
    stack<int> stk;
    stack<int> min_stk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */