class TrieNode:

    def __init__(self):
        self.hash = {}
        self.word = False

class WordDictionary:

    def __init__(self):

        self.start = TrieNode()
        

    def addWord(self, word: str) -> None:

        cur = self.start
        for letter in word:
            if letter not in cur.hash:
                cur.hash[letter] = TrieNode()
            cur = cur.hash[letter]
        cur.word = True

        
        return
        
    def search(self, word: str) -> bool:

        def rec(curr,word):
            for i in range(len(word)):

                if word[i] == '.': # if we reach a . 
                    for obj in curr.hash.values(): # check all possibilities 
                        if rec(obj,word[i+1:]):
                            return True
                    else:
                        return False 

                if word[i] in curr.hash:
                    curr = curr.hash[word[i]]
                else:
                    return False
            else:
                if curr.word == True:
                    return True
                else:
                    return False
        
        return rec(self.start,word)
            
        
