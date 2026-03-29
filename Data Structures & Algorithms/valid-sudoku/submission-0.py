class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # data structures
        c = collections.defaultdict(set)
        r = collections.defaultdict(set)
        s = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in s[(i//3,j//3)]:
                    print(i,j)
                    print('row',r)
                    print('col',c)
                    print('sq',s)
                    return False
                else:
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    s[(i//3,j//3)].add(board[i][j])
        
        return True
                




        