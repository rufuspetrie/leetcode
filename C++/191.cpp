/*
- Can extract lowest bit by taking n & 1 and add to total
- Can progress to higher bits by right-shifting once
*/
class Solution {
public:
    int hammingWeight(int n) {
        int total = 0;
        while(n > 0){
            total += n & 1;
            n >>= 1;
        }
        return total;
    }
};