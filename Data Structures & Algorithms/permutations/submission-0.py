class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(curr,rem):

            #
          

            if len(rem) == 1:
                ans.append(curr + [rem[0]])
                return 
            
            #sc
            for i in range(len(rem)):
                cppy = rem.copy()
                print(cppy)
                r = cppy.pop(i)
                dfs(curr +[r],cppy)


        
        dfs([],nums)
        return ans