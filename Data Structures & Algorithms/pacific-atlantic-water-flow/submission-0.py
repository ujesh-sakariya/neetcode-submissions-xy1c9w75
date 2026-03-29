class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set() # hash sets
        atlantic = set()
      

        def dfs(type,i,j,prev):

            #BC
            # if the cell has already been visted
            if (i,j) in type:
                return
            
            # not in boundary
            if i < 0 or i > row - 1 or j < 0 or j > col - 1:
                return
            #logic if we shouldnt add it
            if heights[i][j] < prev:
                return
            
            #SC
            # not in the set and satisfies conditon
            type.add((i,j))
            curr = heights[i][j]
            # call for all neighbouring cells
            dfs(type,i+1,j,curr)
            dfs(type,i-1,j,curr)
            dfs(type,i,j+1,curr)
            dfs(type,i,j-1,curr)

            return

        # call dfs on only the boarder cells 

        row = len(heights)
        col = len(heights[0])

        for i in range(row):

            for j in range(col):

                # identify pacific
                if i == 0 or j == 0:
                    dfs(pacific,i,j,-1)
                # identify atlantic
                if i == row -1 or j == col-1:
                    dfs(atlantic,i,j,-1)

        final = []
        print(pacific)
        print(atlantic)

        for i in range(row):
            for j in range(col):
                if (i,j) in pacific and (i,j) in atlantic:
                    print(i,j)
                    final.append([i,j])

        return final

                    