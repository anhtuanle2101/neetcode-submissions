class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dictionary to store anagrams being to a group (a tuple representing the freqs of character in the word)
        # translate the word by first having an array of 26 elements representing 26 characters (lower English chars)
        # then convert the array into a tuple
        # check if the tuple exists in the dictionary
        # if yes, append the word into that group
        # else, create a new group being 
        group_anagrams = {}

        for s in strs:
            arr = [0] * 26

            for c in s:
                idx = ord(c) - ord("a")

                arr[idx] += 1
            
            # convert
            group = tuple(arr)

            if group in group_anagrams:
                group_anagrams[group].append(s)
            else:
                group_anagrams[group] = [s]

        return group_anagrams.values()