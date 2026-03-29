class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(nums):
            v1,v2 = 0,0

            for i in range(len(nums)):
                temp = v2 
                v2 = max(v2,nums[i] + v1)
                v1 = temp
            
            return v2

        if len(nums) == 1:
            return nums[0]
        return max(rob(nums[:-1]),rob(nums[1:]))
