class Solution:
    def climbStairs(self, n: int) -> int:

        hash = {}

        def dfs(c,s):
            #BC - alread
            if c in hash:
                return hash[c]

            if c == n:
                return 1
            if c > n:
                return 0
            
            #SC
            s += dfs(c+1,s)
            s += dfs(c+2,s)
            hash[c] = s
            return s 
        
        return dfs(0,0)
               
            

            
            