class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0 

        def find(l,r,i):
                nonlocal count
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count+=1
                    l -=1
                    r+= 1 

        for i in range(len(s)):

            find(i,i,i)
            find(i,i+1,i)

        return count 

            
        

       



        