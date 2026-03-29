class Solution:
    def numDecodings(self, s: str) -> int:

        dp = { len(s) : 1} # store the index : solution values - last value only one way
        # dp[i] = the number of ways to decode substring s[i:]
        # it has a reoccurance r of dp[i] = dp[i+1] (taking i as a single digit) + dp[i+2] (taking i as 2 digits)
        c,v1,v2 =0,1,0
        for i in range(len(s)-1,-1,-1): # starting from the last value

            if s[i] == '0': # if the value is 0, it can't be taken as a single or double digit so we say 0 
                c = 0
            else:
               c = v1 # taking s[i] as a single digit (always valid)
            
            #if we should take it as a double digit or not 
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"): 
                c += v2
            temp = v1
            v1 = c
            v2 = temp
                
        return c



