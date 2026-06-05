class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"#"+s
        
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            len_str = ""
            while s[i] != "#":
                len_str += s[i]
                i += 1
            
            i += 1
            
            len_int = int(len_str)
            cur_str = ""
            for j in range(i, i + len_int):
                cur_str += s[j]
            result.append(cur_str)
            i += len_int
        
        return result

            
            