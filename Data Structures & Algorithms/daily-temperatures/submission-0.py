class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures) 
        c = 0
        while c < len(temperatures):
           
          
            while stack and temperatures[c] > temperatures[stack[-1]]:
                n = stack.pop()
                print(n)
                output[n] = c - n 
            stack.append(c)

            print(stack)
            c+=1
        
        
        return output

                
