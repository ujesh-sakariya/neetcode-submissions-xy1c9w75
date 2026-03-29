class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
        
        dict = {}

        for i in range(len(s)):
            dict[s[i]] = 1 + dict.get(s[i],0)
        for j in range(len(t)):
            if t[j] not in dict or dict[t[j]] == 0:
                return False
            else:
                dict[t[j]] -= 1
        
        return True


        