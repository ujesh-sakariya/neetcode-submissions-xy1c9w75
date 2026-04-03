class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        mappings = {'2': 'abc','3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                 }

        def dfs(curr,index):
            
            #bc
            if index > len(digits) -1 :
                ans.append(curr)
                return
            
            #sc
            c = (mappings[digits[index]])
            print(c)
            for i in range(len(c)):
                dfs(( curr + c[i]),index+1)
        
        if not digits:
            return []
        else:
            dfs('',0)

        return ans
