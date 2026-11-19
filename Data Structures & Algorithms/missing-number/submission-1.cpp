class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // nums is a continuous list of ints ranging 0-n, 
        // monoton inc, one missing num - includes endpoints
        int n = nums.size();
        if (nums.size() == 1) {
            return nums[0] ^ 1;
        }

        std::sort(nums.begin(), nums.end());
        if (nums[0] != 0) return 0;
        for (int i = 1; i< nums.size(); ++i) {
            if (nums[i-1] != nums[i] -1 ) return nums[i] -1 ;
        }
        return nums.size();
    }
};
