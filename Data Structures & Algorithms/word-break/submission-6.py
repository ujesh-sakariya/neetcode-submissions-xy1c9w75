class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        mem = {}

        def dfs(k,s):
            print('function called with',k,s)
            #BC
            if len(s) == 0:
                return True
            
            #BC2
            if k in mem:
                return mem[k]
            #SC

            # for all words
            for i in range(len(wordDict)):
                t0 = 0
                t1 = 0
                while t0 < len(wordDict[i]) and t1 < len(s): # means not found word yer
                    # cases 
                        print('t0 val: ',t0)
                        if wordDict[i][t0] != s[t1]:
                            print(wordDict[i],'not found in',s)
                            break
                        t0+=1
                        t1+=1
                        #1. word matches
                else:
                    if t0 == len(wordDict[i]):
                        print('found with k as',k,'and t1 as',t1)
                        if dfs(t1+k,s[t1:]):
                            return True
                
            mem[k] = False
            return mem[k]
                
        
        return dfs(0,s)


      