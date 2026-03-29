class Solution:
    def rob(self, nums: List[int]) -> int:
        
        v1,v2 = 0,0# v1 max value of 0 to i - 2, v2 max value of 0 to i - 1

        # at evey house, we can either rob the current house and v1 
        # or not rob the current house and take the value of v2 

        for i in range(len(nums)):
            
            temp = v2
            v2 = max(v2, v1 + nums[i])
            v1 = temp
        
        return v2
            

