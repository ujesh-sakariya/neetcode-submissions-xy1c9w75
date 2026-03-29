class Solution:
    def rob(self, nums: List[int]) -> int:
        
        hash = {}

        def dfs(i):
            print('current i isii',i)
            if i >= len(nums):
                return 0

            #BC - if we have solved it already
            if i in hash:
                print('i is in hash')
                return hash[i]
            
            if i + 2 > len(nums):
                print('last one')
                return nums[i]


            #SC
            print('current i is: ',i)
            hash[i] = nums[i] + max(dfs(i+2),dfs(i+3))
            return hash[i]
        
        return max(dfs(0),dfs(1))
            
        

