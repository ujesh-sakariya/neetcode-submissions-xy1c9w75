class Solution:
    def trap(self, height: List[int]) -> int:
        
        w = 0

        for i in range(1,len(height)-1):

            p = max(height[:i])
            s = max(height[i+1:])

            w += max(min(p,s) - (height[i]),0)

        return w
                

        
