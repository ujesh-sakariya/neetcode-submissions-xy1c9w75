class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = '' # store the longest string
        m = len(s) # length of string
        f = -1 # length of current max palindrome
        i = 0 # current index of character

        while i < m:
            l,r = i,i
            while  r < m and s[l] == s[r]: # to check for even and odd
                r+=1
            r-=1

            while l -1  >= 0 and r < m -1 and s[l-1] == s[r+1]: # check for palindrome
                l-=1
                r+=1
            if r - l > f: # check if longest 

                f= r-l

                longest = s[l:r+1]
            i+=1
        
        return longest



        