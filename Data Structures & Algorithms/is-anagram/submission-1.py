class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 hash maps to keep track of freq of each character
        # compare each key of 2 hash maps if they are all matched 
        # - len(hash_map1) == len(hash_map2)
        # - for k in hash_map1 -> hash_map1[k] == hash_map2[k]

        hash_map1 = {k: 0 for k in s}

        for c in s:
            hash_map1[c] += 1

        hash_map2 = {k: 0 for k in t}

        for c in t:
            hash_map2[c] += 1

        if len(hash_map1) != len(hash_map2):
            return False

        for k in hash_map1:
            if k not in hash_map2 or hash_map1[k] != hash_map2[k]:
                return False
        
        return True