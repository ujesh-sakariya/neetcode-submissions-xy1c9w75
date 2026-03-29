class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix
        if len(nums)< 2:
            return [nums[1],nums[0]]
    
        c = nums[0]
        p = [1,nums[0]]
        l = len(nums)

        for i in range(2,l):

            c*= nums[i-1]
            p.append(c)
        
        # suffixes

        s = [nums[l-1],1]
        c = nums[l-1]
        for i in range(l-3,-1,-1):

            c*=nums[i+1]
            s.insert(0,c)
        print(s)
        f = []
        for i in range(l):

            f.append(p[i] * s[i])
        
        return f





        