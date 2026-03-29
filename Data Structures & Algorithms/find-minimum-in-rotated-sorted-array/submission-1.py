class Solution:
    def findMin(self, nums: List[int]) -> int:

        r,l = len(nums)-1, 0
        m = (r + l) // 2
        ans = nums[m]


        while l <= r: # looping condition for binary search

            if nums[l] < nums[r]: # this means that the current array is sorted
                ans = min(ans,nums[l])
                break
                
            m = (l + r) // 2
            ans = min(ans,nums[m]) 
            if nums[m] >= nums[l]:
                l = m + 1 
            else:
                r = m -1 
                            

        return ans


        
        
        


        