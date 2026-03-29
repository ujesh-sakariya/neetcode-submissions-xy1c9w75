class Solution:

    def encode(self, strs: List[str]) -> str:

        final =""
        for word in strs:
            final += str(len(word))+ 'ñ' + word

        print(final)
        return final


                

    def decode(self, s: str) -> List[str]:

        c = 0
        strings =[]
        while c < len(s):            
            letters = ''
            while s[c] != 'ñ':
                letters+=s[c]
                c+= 1
            c+=1

            m = ""
            for i in range(c,c + int(letters)):

                m+= s[i]
                c+=1        
        
            strings.append(m)

        return strings
            
            

               

    

            