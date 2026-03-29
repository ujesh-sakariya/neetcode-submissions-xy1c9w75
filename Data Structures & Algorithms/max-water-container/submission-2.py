class Solution:
    def maxArea(self, heights: List[int]) -> int:

        h,l,u = 0,0,len(heights)-1

        while u > l:
            c = (u-l) * min(heights[u],heights[l])
            print(c)
            if c > h:
                h = c
            if heights[u] > heights[l]:
                l+=1
            else:
                u-=1
        
        return h
        
        