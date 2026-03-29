class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)): 
            # not in the right position
            while (nums[i] - 1) != i:
                # check if the right positon has the correct value already in it 
                if nums[(nums[i]-1)] == nums[i]:
                    return nums[i]
                else:
                    # swap them around
                    temp = nums[i]
                    nums[i] =  nums[(nums[i]-1)]
                    nums[(temp-1)] = temp
                    
            
            