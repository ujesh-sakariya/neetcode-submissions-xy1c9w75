class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalphanumeric(l):
            return ((ord(l) >= 48 and ord(l) <= 57) or 
            (ord(l) >= 97 and ord(l) <= 122) or 
            (ord(l) >=65 and ord(l) <= 90))
          
    

        l,r =0,len(s) -1

        while r > l:
            while r>l and not isalphanumeric(s[l]):
                l+=1
            while r> l and not isalphanumeric(s[r]):
                r-=1
            if s[l].lower() == s[r].lower():
                l,r = l+1,r-1
            else:
                return False
        
        return True
            

                
    

        