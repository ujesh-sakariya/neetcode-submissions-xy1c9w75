import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        length = len(nums)
        # index is the index pos for which we want to know the value for 
        index = length - k 
        
        # left and right pointers allowing us to narrow the window interested in 
        l,r = 0, len(nums) -1

        # when p == index, we have the correct value
        while True:
            p = l

            # we will choose our pivot to 
            # be the last value in the interested window 
            # therefore pivot will always 
            # be the same as the right pointer

            pivot = nums[r]

            for i in range(l,r):

                if nums[i] < pivot:
                    # if the number is less than the pivot, we move it 
                    # to where the current pointer is
                    # we are trying to push all the values less than the
                    # pivot to one side therefore when we make the final
                    # swap, putting the pivot in the correct place 
                    # all the values to the left of it are less than it 
                    # and all the values to the right of it are greater than it 
                    nums[i], nums[p] = nums[p], nums[i] 
                    p+=1

            # do the swapping of the pivot and pointer 
            # this is the exact index the value should be
            nums[p], nums[r] = nums[r], nums[p]

            # resize window to the interested area like binary search
            if index < p:
                r = p - 1 
            elif index > p:
                l = p + 1
            # unless the pivot is the value we are interested in
            else:
                return nums[p]
            


        
        