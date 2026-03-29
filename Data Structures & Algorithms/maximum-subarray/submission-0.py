class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        top,t1,t2 = nums[0],nums[0],nums[0]
       
        for i in range(1,len(nums)):

            t1 = max(t1,t2) + nums[i]
            t2 = nums[i]
            top = max(top,t1,t2)
        
        return top
        