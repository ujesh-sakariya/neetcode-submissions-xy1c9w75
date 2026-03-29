class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        s1hash = {}
        s2hash = {}

        for c in s1: # set up hashset for s1 
            s1hash[c] = 1 + s1hash.get(c,0)


        l,r = 0,0

        while r < len(s2): 

            # ensure only freq of len s1 is ever maintained

            while r -l < len(s1): # fill up the first len s1 letters
                s2hash[s2[r]] = 1 + s2hash.get(s2[r],0)
                r+=1
            
            for key in s1hash.keys():
                print(key)
                if s1hash[key] != s2hash.get(key,-1):
                    break
            else:
                return True
            
            print(s1hash)
            print(s2hash)
            s2hash[s2[l]] -= 1
            l+=1
           

        return False



            