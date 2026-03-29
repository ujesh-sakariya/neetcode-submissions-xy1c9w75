class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # mem
        mem = {}

        def dfs(n):

            #BC
            if n in mem:
                return mem[n]
            
            if n == 0:
                return 0
            
            #SC
            res = 1e9
            for i in range(len(coins)):
                if n >= coins[i]:
                    
                    res = min(1 + dfs(n-coins[i]),res) 
            
            mem[n] = res
            return res

        
        ans = dfs(amount)
        return ans if ans < 1e9 else -1
                

                

            