class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1);
        int offset = 1;
        for (int i = 1; i < n+1; ++i) {
            if (i == offset * 2) offset *= 2;
            result[i] = 1 + result[i - offset];
        }
        return result;
    }
};
