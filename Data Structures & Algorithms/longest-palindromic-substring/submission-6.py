class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ''
        m = len(s) # length of string
        f = 0 # length of current max palindrome
        i = 0 # current index of character
        if m == 1:
            return s
        while i < m:
            l,r = i,i
            while  r < m and s[l] == s[r]:
                r+=1
            r-=1
            print(f'L {l} and r {r} afte finding repeating letters')
            while l -1  >= 0 and r < m -1 and s[l-1] == s[r+1]:
                l-=1
                r+=1
            print(f'l {l} and r {r} afte finding palindrom')
            if r - l >= f:
                print('found')
                f= r-l
                longest = s[l:r+1]
            i+=1
        
        return longest



        