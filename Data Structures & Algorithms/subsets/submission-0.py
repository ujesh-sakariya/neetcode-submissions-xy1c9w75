class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]
        def dfs(curr,index):

            #bc 
            if index == len(nums):
                return
            
            #sc
            for i in range(index,len(nums)):
                # store that arr 
                ans.append(curr + [nums[i]])
                # recurse with that arr
                dfs(curr + [nums[i]],i+1)


        dfs([],0)

        return ans