class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        mem = {}

        for i in range(len(text1),-1,-1):
            mem[(i,len(text2))] = 0
        for i in range(len(text2),-1,-1):
            mem[(len(text1),i)] = 0
        

        print(mem)
        for i in range(len(text1)-1,-1,-1):
      
            for j in range(len(text2)-1,-1,-1):
                print(i,j)
                if text1[i] == text2[j]:
                    mem[(i,j)] = 1 + mem[(i+1,j+1)]
                else:
                    mem[(i,j)] =  max(mem[(i+1,j)],mem[(i,j+1)])

               
        
        return (mem[(0,0)])