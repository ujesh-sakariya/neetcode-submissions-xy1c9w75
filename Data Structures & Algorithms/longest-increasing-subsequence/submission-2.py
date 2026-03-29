class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        for i in range(len(nums)-2,-1,-1):
            c= 1
            for j in range(i,len(nums)):
                if nums[j] > nums[i]:
                    c = max(c,1+dp[j])
            dp[i] = c
            print(dp)

        return max(dp)

