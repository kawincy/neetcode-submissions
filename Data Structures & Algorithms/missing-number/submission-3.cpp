class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // nums is a continuous list of ints ranging 0-n, 
        // monoton inc, one missing num - includes endpoints
        // no sort guarantee
        // figure out closest power of 2 > nums.size() = k 
        // find k by logn multiplications by 2
        // xor every number in nums + pad extras
        // return the result

        // 0001
        // 0010
        // 0011
        // 0100
        // 0101
        // 0110
        // 0111
        // 1000

        int n = nums.size();
        // int n = 6;
        if (nums.size() == 1) {
            return nums[0] ^ 1;
        }

        int k = 2;
        while (k <= n) {
            k *= 2;
        }
        // k -= 1;

        int result = 0;

        for (int num : nums) {
            result ^= num;
        }

        for (int i = nums.size() + 1; i < k; ++i) {
            result ^= i;
        }

        return result;

        // std::cout << "k = " << k << std::endl;

        // printf("%b", 1 ^ 2 ^ 3 ^ 4 ^ 5  ^ 7 ^ 8);

        // naive solution
        // std::sort(nums.begin(), nums.end());
        // if (nums[0] != 0) return 0;
        // for (int i = 1; i< nums.size(); ++i) {
        //     if (nums[i-1] != nums[i] -1 ) return nums[i] -1 ;
        // }
        // return nums.size();
    }
};
