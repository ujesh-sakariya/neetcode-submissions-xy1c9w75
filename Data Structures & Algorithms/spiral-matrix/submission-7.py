class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = []

        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                output.append(matrix[i][0])
            return output

        l,r = 0, len(matrix[0])  # store the param of  length of rows
        top,bottom = 0, len(matrix) # store param of length of col
        print(l,r,top,bottom)
        while bottom > top and l < r:
            for i in range(l,r):
                output.append(matrix[top][i])
            top +=1
            print(output)
            for i in range(top,bottom):
                output.append(matrix[i][r-1])
            r -= 1

            if not (l < r and top < bottom):
                break
            for i in range(r-1,l-1,-1):
                output.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                output.append(matrix[i][l])
            l += 1

        return output

    

            
            

            
