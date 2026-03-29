class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        oldRow = [1] * n
 
        for i in range(m -1):
            row = [1]*n
            for j in range(n-2,-1,-1):

                row[j] = row[j+1] + oldRow[j]
            
            oldRow = row
        
        return oldRow[0]



