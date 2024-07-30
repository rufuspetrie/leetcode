/*
- Notice that it's a lot less work just using arrays of bools instead of vectors/hashes etc
*/
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        const int size = 9;
        bool rows[size][size] = {false};
        bool cols[size][size] = {false};
        bool sqrs[size][size] = {false};
        
        for(int r = 0; r < size; r++){
            for(int c = 0; c < size; c++){
                if(board[r][c] == '.') continue;
                int idx = board[r][c] - '0' - 1;
                int area = (r/3) * 3 + (c/3);
                if(rows[r][idx] || cols[c][idx] || sqrs[area][idx]) return false;
                rows[r][idx] = true;
                cols[c][idx] = true;
                sqrs[area][idx] = true;
            }
        }
        return true;
    }
};