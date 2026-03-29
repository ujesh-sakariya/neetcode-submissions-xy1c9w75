class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1
        m = (l + r) // 2
        while l <=r:
            print('starting m value is ',m)
            if nums[m] == target:

                return m 

          
            if nums[m] >= nums[l]: # T if left side is sorted
                print('left side is sorted')
                if nums[l] > target: # it can't be on the left side and must be on the right 

                    l = m + 1
                    print('cant be on the left')
                else: # check if it is in the range by comparing it to middle

                    if target < nums[m]: # must be in the range

                        r = m -1 
                    
                    else: # does not exist 

                       l = m + 1

                
            else: # right side is sorted

                if target > nums[r]: # must be on left side

                    r = m -1
                
                else: 

                    if target > nums[m]: # must be in range

                        l = m + 1 
                    
                    else:

                        r = m -1


            m = (l + r) // 2
            print('m is now updated to: ',m)

            print(nums[m])
        
      
        
        return -1

