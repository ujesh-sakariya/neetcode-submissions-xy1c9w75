class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans = 0
        for i in range(len(nums)+1):
            ans ^= i
        
        # now we have a value that is comprised of all the values we are looking for

        for i in range(len(nums)):
            ans ^= nums[i]
        
        return ans


        