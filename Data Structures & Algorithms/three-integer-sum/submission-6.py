class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)
        f =[]
        for i in range(len(nums)-1):
            print(nums[i])
            if i> 0 and nums[i] == nums[i-1]:
                continue
            else:
                t,l,u = 0 - nums[i], i+ 1,len(nums) -1
                while u <= len(nums) -1 and l >= i + 1 and u>l:
                    print(l,u)
                    if t - (nums[l]+ nums[u]) > 0:
                        l+=1
                        while nums[l] == nums[l-1] and l < len(nums) -1:
                            l+=1
                    elif t - (nums[l]+ nums[u]) < 0:
                        u-=1
                        while nums[u] == nums[u+1] and u > i + 1:
                            u-=1
                    else:
                        print([nums[i],nums[l],nums[u]])
                        f.append([nums[i],nums[l],nums[u]])
                        l,u = l+1,u-1
                        while nums[l] == nums[l-1] and l < len(nums) -1:
                            l+=1
                        while nums[u] == nums[u+1] and u > i + 1:
                            u-=1
        print(f)
        return f
