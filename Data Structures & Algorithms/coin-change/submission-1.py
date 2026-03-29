class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # bottom up approach 

        
        dp = {i:1e9 for i in range(amount+1)}
        dp [0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],1+dp[i-coin])
            

        return dp[amount] if dp[amount] != 1e9 else -1
                
        