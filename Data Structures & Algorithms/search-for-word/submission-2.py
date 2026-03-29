class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row,column = len(board),len(board[0]) # get the dimensions 
        hash = set()
        def bt(r,c,i):
            nonlocal hash
            #BC
            if i == len(word):
                return True
            if r >= row or r < 0 or c >= column or c < 0: # out of dimension 
                return False
            elif board[r][c] != word[i]: # not the letter needed
                return False
            elif (r,c) in hash: # on a letter that we have already visited
                return False


            
            #SC
            hash.add((r,c))
            res = bt(r+1,c,i+1) or bt(r,c+1,i+1) or bt(r-1,c,i+1) or bt(r,c-1,i+1)
            hash.remove((r,c)) 
            return res

        for i in range(row):
            for j in range(column):

                if board[i][j] == word[0]:
                     if bt(i,j,0):
                        return True
        else:
            return False

            



        