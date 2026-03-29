class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # get all the items in a dict first
        dict = {}
        for i,n in enumerate(nums):
            if (target - n) in dict:
                return sorted([i , dict[target-n]])
            else:
                dict[n] = i
        

       
        