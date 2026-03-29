class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        answer = []
        current = []
        index = 0
      

        def bt(i,total,current):
        
            #BC 
            if total == target: # we have a match
                print('match')
                print(current)
                answer.append(current[:])
                print(answer)
                return
            # out of bounds
            if i >=len(nums) or total > target: 
                return

            #SC
            current.append(nums[i])
            bt(i,total + nums[i],current)
            current.pop()
            bt(i+1,total,current)
            return
        
        bt(0,0,[])
        return answer

        