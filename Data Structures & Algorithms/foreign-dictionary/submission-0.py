


class Solution:

    def foreignDictionary(self, words: List[str]) -> str:
        
        # store nodes if they exist 
        letters = {c:set() for i in words for c in i}
        
        # Go through all the words and detect if there is order
        for i in range(len(words)-1):
            p1,p2 = len(words[i]),len(words[i+1]) 
            c = 0
            while c < p1 and c < p2:

                if words[i][c] == words[i+1][c]: 
                    c+=1
                else:
                    letters[words[i][c]].add(words[i+1][c])
                    break          
            else:
                if p1 > p2:
                    return ''
            
        
        # Finding the order of letters
        visited = set() # we have visited the node already and processed it 
        path = set() # visited on the the current DFS - used for detecting if there is a cycle 
        # WE CAN MERGE VISTED AND PATH INTO ONE E.G VISITED = {} L: TRUE - MEANS VISITED AND IN PATH AND L :FALSE - VISITED BUT NOT IN PATH 
        res = []

        def postOrderDFS(l):

            #BC1 - if we have visited on the path already - cycle
            if l in path:
                return False
            #BC2 - if we have visited before - no need to process it
            if l in visited:
                return True
             
            print('here')
            #SC 
            path.add(l) # visited on current dfs
            visited.add(l) # visited before
            for x in letters[l]:
                if not postOrderDFS(x):
                    print('got here')
                    return False
            res.append(l) # post OrderDFS means we add it after we have recursed through
            print(res)
            path.remove(l)
            return True

        print(letters)
        for l in letters.keys():
            print(l)
            if not postOrderDFS(l):
                return ''
        res.reverse()
        return ''.join(res)

            
            
            


            
        

                    

                    

