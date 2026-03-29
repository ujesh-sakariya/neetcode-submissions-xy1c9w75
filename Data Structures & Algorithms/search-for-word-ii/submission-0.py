class TrieNode():
    def __init__(self):
        self.Map = {}
        self.valid = False
        self.index = -1
class Solution:
    def __init__(self):
        self.start = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # dimension of the board
        row = len(board)  
        col = len(board[0])

        # prevent repetitions
        visited = set()
        
        # store answer
        ans = []

        def add_word(word,i):
            ''' function to add the word '''
            curr = self.start
            for letter in word:
                if letter not in curr.Map:
                    curr.Map[letter] = TrieNode()
                curr = curr.Map[letter]
            curr.valid = True
            curr.index = i
        
        # add all the words to the trie DS
        for i,word in enumerate(words):
            add_word(word,i)

        def dfs(i,j,curr):

            #BC1 if out of bounds
            if i < 0 or i > row -1 or j < 0 or j > col -1:
                return
            
            #BC2 if already visited
            if (i,j) in visited:
                return 

            #BC2 if not the letter we are looking for
            if board[i][j] not in curr.Map:
                return
            
            #BC3 if the word is a valid word
            if curr.Map[board[i][j]].valid == True and curr.Map[board[i][j]].index != -1:
                ans.append(words[curr.Map[board[i][j]].index])
                curr.Map[board[i][j]].index = -1
                # we don't return as can carry on e.g back and backend


            #SC
            visited.add((i,j))
            curr = curr.Map[board[i][j]]
            dfs(i+1,j,curr)
            dfs(i-1,j,curr)
            dfs(i,j+1,curr)
            dfs(i,j-1,curr)
            visited.remove((i,j))
        
        for i in range(row):
            for j in range(col):
                if board[i][j] in self.start.Map:
                    dfs(i,j,self.start)
        
        return ans

        





                        


        

        