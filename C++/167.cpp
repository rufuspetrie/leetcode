/*
- Initial solution: find largest j and slide i forward
- Cleaner solution: slide i/j at each step as it's a binary choice - requires less while's
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        vector<int> result;

        while(i < j){
            if(numbers[i] + numbers[j] < target){
                i++;
            }
            else if(numbers[i] + numbers[j] > target){
                j--;
            }
            else{
                result.push_back(i + 1);
                result.push_back(j + 1);
                break;
            }
        }
        return result;
    }
};