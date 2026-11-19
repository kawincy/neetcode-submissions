class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // result is minimum of dp[-1] or dp [-2]
        // min(dp[ i - 1]+  cost[i-1], dp[ i - 2] + cost[i-2] ) 
        int dp[cost.size() + 1];
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 2; i < cost.size() + 1; ++i) {
            dp[i] = std::min(dp[i - 1] + cost[i-1],
                             dp[i - 2] + cost[i-2]);
            std::cout << dp[i] << std::endl;
        }
        return dp[cost.size()];
    }
};
