class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       

        
        c,l = 1, len(nums)
        f = [0] * l

        for i in range(l):

            f[i] = c
            c*= nums[i]
        
        # postfix
        s = 1
        for i in range(l-1,-1,-1):

            f[i] *= s
            s*=nums[i]
        
        return f





        