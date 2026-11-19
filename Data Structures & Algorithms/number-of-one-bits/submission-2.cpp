class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint8_t result = 0;
        // for (int i = 0; i < 32; ++i) {
        //     if ((n >> i) & 0b1) ++result;
        // }
        while (n) {
            n &= n-1;
            ++result;
        }
        return result;
    }
};
