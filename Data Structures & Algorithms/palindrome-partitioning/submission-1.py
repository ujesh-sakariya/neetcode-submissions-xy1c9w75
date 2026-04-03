class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        def dfs(curr,i,j):

            #bc
            if i == len(s) -1:
                print(i,j)
                if check(s[j:i+1]):
                    print(curr)
                    curr.append(s[j:i+1])
                    ans.append(curr[:])
                    curr.pop()
                return
            
            #sc
            
            #right --> continue to build the substring
            dfs(curr,i+1,j)
            # left --> consider if current substring is a palindrome or not
            if check(s[j:i+1]):
                curr.append(s[j:i+1])
                i+=1
                j = i
                dfs(curr,i,j)
                curr.pop()
            else:
                return
        
        def check(p):
            l = 0
            r = len(p) -1

            while l <= r:
                if p[l] == p[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        
        dfs([],0,0)
        print(ans)
        return ans

            