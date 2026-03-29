class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # the index is the number of occ of a number
        # max number is length of list
        count = [[] for i in range(len(nums)+1)]
        # store the num and the num of occ
        pair = {}
        for i in range(len(nums)):
           
            pair[nums[i]] = 1 + pair.get(nums[i],0)

       # for each num store the number in index occ
        for key,value in pair.items():
            (count[value]).append(key)
            print(count)

        

        ans =[]
        for j in range(len(count)-1 ,-1,-1):

            if len(ans) < k:
                
                if count[j] != []:

                    for m in range(len(count[j])):
                        ans.append(count[j][m])
                        print(len(ans))
                        print(k)
       
        return ans