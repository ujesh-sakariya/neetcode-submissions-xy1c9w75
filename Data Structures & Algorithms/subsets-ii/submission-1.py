class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        def dfs(curr,index):

            #bc
            if index >= len(nums):
                print(ans)
                ans.append(curr[:])
                return

            print(index)
            #sc
            curr.append(nums[index])
            dfs(curr,index+1)
            curr.pop()
            while index < (len(nums) - 1) and nums[index] == nums[index+1]:
                print(index)
                index +=1
            dfs(curr,index+1)

        dfs([],0)

        return ans
