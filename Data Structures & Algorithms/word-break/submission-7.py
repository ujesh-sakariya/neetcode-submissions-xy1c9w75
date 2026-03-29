class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # because if we get to the last position, we have reached the end of the string

        for i in range(len(s)- 1,-1,-1):

            # now we need to check if a valid word can go there starting at index i 

            for w in wordDict:
                # first check length
                if len(w) <= (len(s) - i) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        print(dp)
        return dp[0] 
            
            

