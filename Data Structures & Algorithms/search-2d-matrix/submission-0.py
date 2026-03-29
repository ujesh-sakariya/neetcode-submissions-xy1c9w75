class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            # must be in this row 
            if matrix[i][0] <= target <= matrix[i][-1]:
                #binary search on that roow
                l = 0
                r = len(matrix[i]) -1 
                while l <= r:
                    m = (l + r) // 2
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] > target:
                        r = m -1
                    else:
                        l = m + 1
                    
                    m = (l+r) // 2
                return False
                

        else:
            return False
        
