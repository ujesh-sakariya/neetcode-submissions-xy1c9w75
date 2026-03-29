class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        steps = 0
        c= 0
        while c + nums[c] < len(nums) -1:
            print(c,nums[c])
            bestindex = 0 
            bestval = 0
            for i in range(c,c+nums[c]+1):
                if i + nums[i] > bestval:
                    print(i,nums[i])
                    bestindex = i
                    bestval = i + nums[i]
                
            c = bestindex
            steps+=1
            print(c)
    
        return steps + 1
        
        
        

