class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end = True        

    def search(self, word: str) -> bool:
        #some backtracking
        current = self.root

        def find(node, i):
            if i == len(word):
                return node.end
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if find(child, i+1):
                        return True
                return False
            if c not in node.children:
                return False
            return find(node.children[c], i+1)


        return find(current, 0)
        
        
            
        
