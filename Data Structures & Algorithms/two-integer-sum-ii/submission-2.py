class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        u = len(numbers) -1
        while True:
            print(l,u)
            print(target - (numbers[l] + numbers[u]))
            if (target - (numbers[l] + numbers[u])) > 0:
                l+=1
            elif (target - (numbers[l] + numbers[u])) < 0:
                u-=1
            else:
                return[l+1,u+1]

        
        