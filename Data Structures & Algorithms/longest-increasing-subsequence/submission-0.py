class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            c = 1
            for j in range(i): #only need to consider the numbers in front of it
                if nums[j] < nums[i]:
                    c = max(1 + dp[j],c)
            dp[i] = c

        return max(dp)

