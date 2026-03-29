class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxStep = 0
        curr = -1
        while curr != len(nums)-1:
            print(curr,maxStep)
            if curr < maxStep:
                curr +=1
                maxStep = max(maxStep,curr + nums[curr])
            else:
                print('got here',curr,maxStep)
                break
        else:
            print('got here')
            return True
        
        return False
        