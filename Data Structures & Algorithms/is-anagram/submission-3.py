class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 hash maps to keep track of freq of each character
        # compare each key of 2 hash maps if they are all matched 
        # - len(hash_map1) == len(hash_map2)
        # - for k in hash_map1 -> hash_map1[k] == hash_map2[k]

        # optimization: make use of only one hash map instead of 2 
        # hash_map run through each character in s to store the freqs first
        # then run through the characters in t, if the c not in the hash map => not a valid anagram
        # otherwise, reduce the freq of c in hash map, if freq of c becomes negative => not a valid anagram
        # after the loop finishes, if len(hash_map) == 0, which means all freqs are matched => valid anagram

        hash_map1 = {k: 0 for k in s}

        for c in s:
            hash_map1[c] += 1

        for c in t:
            if c not in hash_map1:
                return False
            
            hash_map1[c] -= 1

            if hash_map1[c] == 0:
                del hash_map1[c]
        
        return len(hash_map1) == 0