class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    ''' 
        insert the word into the prefix tree
        - go by each character
            - check if it is in current node children
                - if not, create a node, set this node to be a children of cur
            - go to the children node
        - set last node (cur) word to true to mark is this end of a complete word
    '''
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                new_node = Node()
                cur.children[c] = new_node

            cur = cur.children[c]
        
        cur.word = True

    ''' 
        - return whether the complete word is in the trie 
        - go by each character
            - if the character is not in the cur children
                - return False
            - go the children node

        - return if the last node (cur) marked work as True -> this is a complete word in Trie
    '''
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
        