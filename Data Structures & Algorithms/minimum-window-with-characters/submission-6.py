class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        thash = {} # hash for t
        for l in t:
            thash[l] = 1 + thash.get(l,0)
        
        shash = {} # hash for s
        for l in s:
            shash[l] = 1 + shash.get(l,0)

        # base case
        for l in t:
            if shash.get(l,0) < thash[l]:
                return ''
        
        # sliding window approach 
        shash.clear()

        matches = 0
        needed = len(thash)
        substring = s
        l=0
        for r in range(len(s)):

            shash[s[r]] = 1 + shash.get(s[r],0)

            if shash[s[r]] == thash.get(s[r],0):
                matches +=1

            if matches == needed:
                
            
                while matches == needed: # shortening the string untill shortest valid in that area
                    print(substring)
                    print(len(s[l:r+1]))
                    if len(s[l:r+1]) < len(substring): substring = s[l:r+1]
                    print(substring)
                    shash[s[l]] -= 1
                    if shash[s[l]] < thash.get(s[l],0): # checks if we have shortended too much
                        print(shash) 
                        print(thash)
                        matches -= 1 
                    l+=1
        
        return substring

                        
                    


            


        

        
