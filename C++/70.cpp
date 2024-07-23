/*
- For n steps, the solution equals the associated Fibonacci number
*/
class Solution {
public:
    int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int a = 1, b = 2, temp = 0;
        for(int i = 2; i < n; i++){
            temp = b;
            b = a + b;
            a = temp;
        }
        return b;
    }
};