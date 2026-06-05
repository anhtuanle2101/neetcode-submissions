class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1

        for c in t:
            if c not in hash_map:
                return False
            hash_map[c] -= 1
            if hash_map[c] == 0:
                del hash_map[c]

        return False if len(hash_map) > 0 else True