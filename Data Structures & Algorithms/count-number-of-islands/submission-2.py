class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0

        row = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            #BC
            # we reach the boundaries
            if i < 0 or i > row -1 or j < 0 or j > col -1:
                return
            # if we have already visited the node
            if (i,j) in visited:
                return
            # we reach a 0 
            if grid[i][j] == '0':
                return
            
            #SC
            print(i,j)
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
            

        for i in range(row):

            for j in range(col):
                if (i,j) not in visited: # not searched yet
                    if grid[i][j] == '1': # island
                        dfs(i,j)
                        print('found on',(i,j))
                        islands +=1
        
        return islands
                    


        