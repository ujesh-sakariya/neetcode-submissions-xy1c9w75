class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        thash = {} # hash for t
        shash = {} # hash for window
        for l in t:
            thash[l] = 1 + thash.get(l,0)
              
        
        # sliding window approach 
        matches = 0
        needed = len(thash)
        substring = s
        l=0
        ans = ''
        for r in range(len(s)):

            shash[s[r]] = 1 + shash.get(s[r],0)

            if shash[s[r]] == thash.get(s[r],0):
                matches +=1

            if matches == needed:
                
                while matches == needed: # shortening the string untill shortest valid in that area
                    print(len(s[l:r+1]))
                    if len(s[l:r+1]) < len(substring): substring = s[l:r+1]
                    shash[s[l]] -= 1
                    if shash[s[l]] < thash.get(s[l],0): # checks if we have shortended too much
                        matches -= 1 
                    ans = substring
                    l+=1
        
        return ans

                        
                    


            


        

        
