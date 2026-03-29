import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        length = len(nums)
        # index is the index pos for which we want to know the value for 
        index = length - k 
        
        # left and right pointers 
        l,r = 0, len(nums) -1

        # when l == index, we have the correct value
        while True:
            p = l
            # starting pivot
            # pivot will always be the same as the right pointer
            pivot = nums[r]

            for i in range(l,r):
                if nums[i] < pivot:
                  
                    # if the number is less than the pivot, we move it 
                    # to where the current pointer is
                    # we are trying to push all the values less than the
                    # pivot to one side 
                    nums[i], nums[p] = nums[p], nums[i] 
                    p+=1
            # do the swapping of the pivot and pointer 
            # this is the exact index the value should be
            print(l,r,p) 
            nums[p], nums[r] = nums[r], nums[p]

            if index < p:
                r = p - 1 
            elif index > p:
                l = p + 1
            else:
                return nums[p]
            


        
        