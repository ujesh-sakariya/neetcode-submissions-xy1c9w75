class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0 
        r = len(matrix) -1
        while l <= r: 
            # must be in this row 
            m1 = (l + r) // 2
            if matrix[m1][0] <= target <= matrix[m1][-1]:
                #binary search on that roow
                l = 0
                r = len(matrix[m1]) -1 
                while l <= r:
                    m2 = (l + r) // 2
                    if matrix[m1][m2] == target:
                        return True
                    elif matrix[m1][m2] > target:
                        r = m2 -1
                    else:
                        l = m2 + 1
                    
                    m2 = (l+r) // 2
                return False
            elif target < matrix[m1][0]:
                r = m1 -1 
            else:
                l= m1 + 1
            m1 = (l + r) // 2
        return False    


    
        
