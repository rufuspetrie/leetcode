/*
- The reason why you move the left pointer over whenever you have a negative investment
- is because you can consider the negative investment as a prefix to the next one
- I.e. that investment will never increase the value of a subsequent investment
- and you have exhausted all investments using the left pointer
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 0, out = 0;
        while(r < prices.size()){
            if(prices[l] < prices[r]) out = max(out, prices[r] - prices[l]);
            else l = r;
            ++r;
        }
        return out;
    }
};