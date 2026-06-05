class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

    def search_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.word == True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.tri = Trie()
        self.board = board
        self.rows, self.cols = len(board), len(board[0])
        for word in words:
            self.tri.insert(word)
        self.result = []
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] in self.tri.root.children:
                    self.cur = ""
                    self.visit = set()
                    self.dfs(i, j, self.tri.root)

        return list(set(self.result))

    def dfs(self, i, j, node):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or (i, j) in self.visit:
            return 
        
        if self.board[i][j] not in node.children:
            return
       
        self.visit.add((i, j))
        node = node.children[self.board[i][j]]
        self.cur += self.board[i][j]

        if node.word == True:
            self.result.append(self.cur[:])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for dr, dc in directions:
            cr, cc = i + dr, j + dc
            self.dfs(cr, cc, node)
                
        self.cur = self.cur[:-1]
        self.visit.remove((i, j))
        

        


        

