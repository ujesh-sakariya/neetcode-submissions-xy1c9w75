class Solution:
    def climbStairs(self, n: int) -> int:

        hash = {}

        def dfs(c) :
            #BC - alread
            if c in hash:
                return hash[c]

            if c == n:
                return 1
            if c > n:
                return 0
            
            #SC
            hash[c] = dfs(c+1) + dfs(c+2)
            return hash[c]
        
        return dfs(0)
               
            

            
            