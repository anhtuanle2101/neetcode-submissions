class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        self.word = word
        return self.dfs(0, self.root)

    def dfs(self, j, root):
        cur = root

        for i in range(j, len(self.word)):
            c = self.word[i]
            if c != ".":
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            else:
                for child in cur.children.values():
                    if self.dfs(i + 1, child):
                        return True
                return False
            
        return cur.word == True

    
