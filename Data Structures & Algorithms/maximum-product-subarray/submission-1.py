class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)

        mi,ma = nums[0],nums[0]

        for i in range(1,len(nums)):

            if nums[i] == 0:
                mi,ma = 1,1
            x,y = nums[i] * mi, nums[i] * ma
            mi = min(x,y,nums[i])
            ma = max(x,y,nums[i])

            res = max(ma,res)
        
        return res
        