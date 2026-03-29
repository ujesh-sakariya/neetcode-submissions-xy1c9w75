class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        s1hash = {}
        s2hash = {}

        matches =0

         # set up hashmap for s1 
        for c in s1:
            s1hash[c] = 1 + s1hash.get(c,0)
        
        # set up hashsmap for s2
        for i in range(len(s1)):
            s2hash[s2[i]] = 1 + s2hash.get(s2[i],0)

        # check the starting matchies from a-z
        for i in range(26):
           if s1hash.get((chr(ord('a') + i)),0) == s2hash.get((chr(ord('a') + i)),0):
            matches +=1
        
        if matches == 26:
            return True

        print(matches)
        l,r = 0,len(s1)

        while r < len(s2): 

            
            print(s1hash)
            print(s2hash)

            s2hash[s2[l]] -= 1
           

            if s2hash[s2[l]] == s1hash.get(s2[l],0):
                matches += 1
            elif s2hash[s2[l]] == s1hash.get(s2[l],0) -1 :
                matches -= 1

            # update the right pointer
            s2hash[s2[r]] = 1 + s2hash.get(s2[r],0)

            if s2hash[s2[r]] == s1hash.get(s2[r],0):
                matches += 1

            elif s2hash[s2[r]]  == s1hash.get(s2[r],0) + 1:
                matches -= 1

            
            
            print(matches)
            r+=1
            l+=1
            if matches == 26:
                return True

           

        return False



            