class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["a","b","cd"]
        # => 1#a1#b2#cd 
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s

        return res

    def decode(self, s: str) -> List[str]:
        cur = 0
        res = []
        while cur < len(s):
            # extract number 
            num = ""
            while s[cur] != "#" and cur < len(s):
                num += s[cur]
                cur += 1

            # pass the special character
            cur += 1
            # extract the word
            word = ""
            for i in range(cur, int(num)+cur):
                word += s[i]
            cur += int(num)
            res.append(word)

        return res

            