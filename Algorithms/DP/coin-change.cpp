// question link: https://leetcode.com/problems/coin-change/

#include<vector>
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int max = amount + 1;
        std::vector<int> dp(amount + 1, max);
        dp[0] = 0;
        for(int i = 1; i < amount + 1; i++){
            for(auto& coin: coins){
                if(i - coin >= 0){
                    dp[i] = std::min(dp[i-coin] + 1, dp[i]);
                }
            }
        }
        return dp[amount] == max ? -1 : dp[amount];
    }
};
