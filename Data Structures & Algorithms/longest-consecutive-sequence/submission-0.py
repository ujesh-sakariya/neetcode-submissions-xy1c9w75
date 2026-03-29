class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # hashset
        h = set(nums)
        ans = 0
        
        
        for n in nums:

            if (n-1) not in h:
                l = 1
                c = n
                while c + l in h:
                    l+=1
                else:
                    ans = max(l,ans)
                    
        
        return ans
                    


        