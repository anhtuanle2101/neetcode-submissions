'''
    board char[[]]
    rows, cols = len(board), len(board[0])
    horizontally and vertically directions = (0,-1), (0,1), (-1,0), (1,0)
    - return all words present in the board
    - provided valid words

    - build a Trie out of all the valid words -> efficient search for the word 

    

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()
        self.cur = []
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        self.words = words
        self.visit = set()

        # build the trie
        self.trie_root = TrieNode()

        for word in words:
            cur_node = self.trie_root
            for c in word:
                if c not in cur_node.children:
                    cur_node.children[c] = TrieNode()
                cur_node = cur_node.children[c]

            cur_node.word = True

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] in self.trie_root.children:
                    self.visit = set()
                    self.cur = []
                    self.backtrack(r, c, self.trie_root.children[board[r][c]])

        return list(self.result)

    '''
        - traverse through each cell in board
        - at r, c, if board[r][c] in root.children:
            -> start traverse
                - if current node marked as a word:
                    add the word to the result
                - mark visited
                - 4 directions to choose from
                    - the new cell is valid only if 
                        - in bound [0, rows] and [0, cols]
                        - never visited (use set)
                        - next character is also a part of current node's children -> part of a valid
                        word
                            -> move forward with next character
                            - backtrack
    '''
    def backtrack(self, r, c, cur):  
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        self.cur.append(self.board[r][c])
        self.visit.add((r, c))
        if cur.word:
            self.result.add("".join(self.cur[:]))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # choose valid path to go
            if nr in range(self.rows) and nc in range(self.cols) and (nr, nc) not in self.visit and cur.children and self.board[nr][nc] in cur.children:
                child = cur.children[self.board[nr][nc]]
                self.backtrack(nr, nc, child)
                self.visit.remove((nr, nc))
                self.cur.pop()



