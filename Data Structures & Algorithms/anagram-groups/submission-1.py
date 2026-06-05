class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()

        def hash(ss):
            freq_counter = [0] * 26
            for c in ss:
                index = ord(c) - ord("a")
                freq_counter[index] += 1
            
            return tuple(freq_counter)

        for ss in strs:
            key = hash(ss)

            if key not in result:
                result[key] = []
            
            result[key].append(ss)

        return list(result.values())
