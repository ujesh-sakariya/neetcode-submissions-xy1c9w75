class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      # using answer - sliding window approch 

        hash = {}
        m = 0
        l,r = 0,0 # window barriers

        while l <= r and r < len(s): # conditons for the slinding window

            hash[s[r]] = 1 + hash.get(s[r],0)

            if (r - l + 1) - max(hash.values()) <= k:
                print(hash)
                print(r,l)
                m = max(m,(r-l+1))

                r+=1
            else:
                hash[s[l]] -= 1
                print(hash)
                l+=1
                r+=1

        return m

                    
            

            
            

        