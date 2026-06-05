class Solution:
    def __init__(self):
        self.separator = "#"

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            str_len = len(s)
            encoded_string += str(str_len) + self.separator + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strings = []
        while i < len(s):
            str_len = ""

            while i < len(s) and s[i] != self.separator:
                str_len += s[i]
                i += 1
            
            str_len = int(str_len)
            next_str = s[i + 1: i + str_len + 1]

            decoded_strings.append(next_str)

            i += str_len + 1
        
        return decoded_strings


    