class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.m = {"2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]}

        self.result = []
        self.cur = []
        self.s = digits

        self.dfs(0)
    
        return self.result

    def dfs(self, i):
        if i == len(self.s):
            if len(self.cur) > 0:
                self.result.append("".join(self.cur[:]))
            return

        cur_digit = str(self.s[i])
        for c in self.m[cur_digit]:
            self.cur.append(c)
            
            self.dfs(i+1)

            self.cur.pop()