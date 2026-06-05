'''
    encode -> put list of strings into a singular string
    - can use a delimiter to seperate the strings in the result. However, if there is a character same as the delimiter, this would break -> 
    wrong decode
    - what we can do here is to insert the len of each word before each
    string and between the len and the string there should be a delimiter
    to seperate them, now if there is a same character followed by the
    delimiter, it won't be an issue since we can just count the first one
    to be the delimiter

    decode -> put a singular string back to list of original strings
    - now for each word, we are expecting the len of the next string followed
    by the demiliter folowed by the next string
    
'''

class Solution:
    def __init__(self):
        self.delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        single_string = ""
        for s in strs:
            single_string += f"{len(s)}{self.delimiter}{s}"
        
        return single_string
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            string_len = ""
            while s[i] != self.delimiter and i < len(s):
                string_len += s[i]
                i += 1
            i += 1
            c = 0
            string_len_int = int(string_len)
            result.append(s[i:i+string_len_int])

            i += string_len_int
    
        return result
            
