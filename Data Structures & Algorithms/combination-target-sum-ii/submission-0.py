class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        def dfs(arr,curr,index,prev):

             #BC  
            if curr == 0:
                ans.append(arr)
                return

            #BC
            if curr < 0 or index > len(candidates)-1:
                return
           
            #SC
            c = candidates[index]
            dfs(arr,curr, index + 1,c)

            if c == prev:
                return
            dfs(arr + [c],curr - c, index + 1,prev)
           

        
        dfs([],target,0,-1)

        return ans
            
