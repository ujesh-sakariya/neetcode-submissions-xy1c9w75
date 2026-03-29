class Solution:
    def isValid(self, s: str) -> bool:
        
        combos = {"(":")","{":"}","[":"]"}
        stack = []
        for i in range(len(s)):

            if s[i] in combos:

                stack.append(s[i])

            else:
               
                    if not stack or combos[stack.pop()] != s[i]:
                        return False
                
        
        if len(stack) !=0:
            return False
        
        return True

