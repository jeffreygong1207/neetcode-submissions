class TrieNode:
     def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:


    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end = True


    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            #otherwise leter is there
            else:
                #keep going
                current = current.children[letter]
        return current.end

        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            else:
                #keep going
                current = current.children[letter]
        return True


        
        