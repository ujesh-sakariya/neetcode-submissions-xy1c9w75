class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = 0 
        row = len(grid)
        col = len(grid[0])

        visited = set()

        def dfs(i,j):
            nonlocal m

            #BC1 - already visited

            if (i,j) in visited:
                return 0

            #BC2 - out of bounds

            if i < 0 or i >= row or j < 0 or j >= col:
                return 0

            #BC3 - if it is a 0

            if grid[i][j] == 0:
                return 0
            
            #SC
            visited.add((i,j))
            
            c = 1 + dfs(i+1,j) +  dfs(i-1,j) + dfs(i,j+1) +  dfs(i,j-1)
            m = max(c,m)
            return c
          
           

        for i in range(row):
            for j in range(col):

                if (i,j) not in visited and grid[i][j] == 1:
                    dfs(i,j)
                else:
                    visited.add((i,j))
        
        return m

                    

'''grid=
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]  '''      




            
        