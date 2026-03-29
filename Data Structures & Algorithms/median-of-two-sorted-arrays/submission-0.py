class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

      # decide which is bigger and which is smalleer   
        if len(nums1) > len(nums2):
            b = nums1
            s = nums2
        else:
            b = nums2
            s = nums1

        # get the total length so we know how many values are on the left and right of the medium
        total = len(s) + len(b)
        half = total // 2

        l,r = 0, len(s) - 1 
        
        while True:
            i = (l+r) // 2 # midpoint for s
            j = half - i - 2  # midpoint for b, 1 for index at 0 and 1 for midpoint stuff

            # this is the logic to chekc if the partitions are correct or not 
            # we make use of the infinities to handle edge cases when completely bigger or not 
            sleft = s[i] if i >=0 else float("-infinity") # if s is entirely smaller
            sright = s[i+1] if (i+1) < len(s) else float('infinity') # if s is entirely bigger
            bleft = b[j] if j >=0 else float("-infinity") # s is entirely bigger than b
            bright = b[j+1] if (j+1) < len(b) else float('infinity') # s is entirely smaller than b 
        

            if sleft <= bright and bleft <= sright:
                if total % 2:
                    return min(sright,bright)
                else:
                    return (max(sleft,bleft) + min(sright,bright)) / 2
            elif sleft > bright:
                r = i - 1
            else:
                l = i + 1


    

