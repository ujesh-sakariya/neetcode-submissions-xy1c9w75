class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        #first iteration check  the row / columns need to be set to 0 
        # before we loop, need to check top row and left most column as we are storing values there
        temp = matrix[0][0] if 0 not in matrix[0] else 0

        for i in range(len(matrix[0])):
            matrix[0][i] = 0 if any(matrix[j][i] == 0 for j in range(len(matrix))) else matrix[0][i]
            print(matrix)
        for i in range(1,len(matrix)):
            matrix[i][0] = 0 if 0 in matrix[i] else matrix[i][0]
            print(matrix)
        
        # check rows if we need to set to 0
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] *len(matrix[i])
        # check cols if we need to set to 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        # check temp if we need to set the top row to 0
        if temp == 0:
            matrix[0] = [0] * len(matrix[0])

        