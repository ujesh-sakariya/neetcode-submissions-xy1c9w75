class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        f = 0 # starting index
        c = 0 # current length
        m = 0 # max length found so far
        hash = defaultdict(lambda: -1)

        for i in range(len(s)):
            print(c)
            if hash[s[i]] < f:

                hash[s[i]] = i
                c+=1
                
            else:
                if c> m: 
                    m= c
                p = f
                f = hash[s[i]] + 1
                hash[s[i]] = i
                c = c - (f - 1 - p)
        
        print(hash)
        if c> m: 
            m=c
            return m
        else:
            return m 




