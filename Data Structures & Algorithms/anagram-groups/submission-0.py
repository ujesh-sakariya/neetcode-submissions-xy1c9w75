class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # approach we use is by having an array as the key which contains the unique 
        # mapping of the number of occurances of each character 
        # value is all the words in the anagram 

        res = defaultdict(list) # this makes the defualt value a list for any new key

        for s in strs:
            # array that stores the occurances of each character in a word
            count = [0] * 26 # initial array has 26 0's

            # go for each character
            for letter in s:
                count[ord(letter) - 97] += 1
            # key needs to be immutable
            res[tuple(count)].append(s) # add it to the array value

        x = list(res.values())
        print(x)
        return x
     

        