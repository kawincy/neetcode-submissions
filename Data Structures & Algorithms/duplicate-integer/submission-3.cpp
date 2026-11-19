class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // std::unordered_set<int> s;
        // for (int i = 0; i < nums.size(); ++i) {
        //     if (s.find(nums[i]) != s.end()) return true;
        //     s.insert(nums[i]);
        // }
        // return false;
        if (nums.empty()) return false;
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
};