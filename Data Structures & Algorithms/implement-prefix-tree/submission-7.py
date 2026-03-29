class PrefixTree:

    def __init__(self):
        self.h = {}

    def insert(self, word: str) -> None:

        def dfs(h,i):
            #BC
            if not h.get(word[i],False):
                h[word[i]] = {} # if the letter is not in the hash map 
            if  i == len(word) -1:
                h[word[i]]['Flag'] = True # if we have reached the end of the word and flag is not T
                return 
            #SC
            return dfs(h[word[i]],i+1)
        
        dfs(self.h,0)




    def search(self, word: str) -> bool:

        def dfs(h,i):
            #BC
            if word[i] not in h:
                return False # letter is not in hash table
            if i == len(word) - 1:
                if h[word[i]].get('Flag',False) == True:
                    return True  # either found the word 
                else:
                    return False # not a valid word
            
            #SC
            return dfs(h[word[i]],i+1)
        
        return dfs(self.h,0)
        
    def startsWith(self, prefix: str) -> bool:

        def dfs(h,i):
            print(prefix[i],i)
            #BC
            if not h.get(prefix[i],False):
                print('FALSE')
                return False # letter is not in hash table
                
            if i == len(prefix) - 1:
                print('TRUE')
                return True # if the prefix exists
            
            #SC
            return dfs(h[prefix[i]],i+1)
        
        return dfs(self.h,0)
            

