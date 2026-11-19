class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // keys are numbers in the array
        // values are the indices
        std::unordered_map<int,int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.contains(target - nums[i])) {
                return std::vector<int> {m[target - nums[i]], i};
            }
            m[nums[i]] = i;
        }
        return std::vector<int>();
    }
};
