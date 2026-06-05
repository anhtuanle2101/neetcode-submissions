class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            count = len(s)
            result += str(count)+"#"+s
        print(result)
        return result
        
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        count = ""
        while i < len(s):
            while s[i] != "#" and i < len(s):
                count += s[i]
                i += 1
            count = int(count)
            if i >= len(s):
                break
            next_str = ""
            for j in range(i+1, i + count + 1):
                next_str += s[j]

            result.append(next_str)
            i += count + 1
            count = ""
        
        return result