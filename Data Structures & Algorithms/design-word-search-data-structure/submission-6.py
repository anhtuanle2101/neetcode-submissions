class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    '''
        add word to ds
    '''
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.word = True

    '''
        return if word match any words in ds
        '.' can be matched to any letter
        - go by each character in finding word
            - if character is not '.'
                - check if character is children of cur node
                    - if not return False
                - keep going to the children node
            - else '.' can match to any characters:
                - go through all the children of the cur node
                    - skipping the current node and the next character in word
                    -> dfs(i + 1, child)                    
    '''
    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root

            for j in range(i, len(word)):
                if word[j] != ".":
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
                else:
                    for c in cur.children:
                        if dfs(j + 1, cur.children[c]):
                            return True
                    return False
            return cur.word
        
        return dfs(0, self.root)

