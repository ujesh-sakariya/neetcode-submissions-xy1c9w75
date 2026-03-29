class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        MSB = 1
        for i in range((n)+1):
            if i == 0:
                ans.append(0)
            else:
                if i == MSB * 2:
                    MSB = MSB * 2
                ans.append(1 + ans[i-MSB])

        return ans
        
            



