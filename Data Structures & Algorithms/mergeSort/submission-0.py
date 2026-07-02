# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        self.sort(pairs, 0, len(pairs) - 1)

        return pairs

    def sort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        middle = s + (e - s) // 2
    
        self.sort(pairs, s, middle)
        self.sort(pairs, middle + 1, e)
    
        self.merge(pairs, s, middle, e)

        return pairs
    
    def merge(self, pairs, s, m, e):
        l = r = 0
        n = s
        L = pairs[s: m + 1]
        R = pairs[m + 1: e + 1]

        while l in range(len(L)) and r in range(len(R)):
            if L[l].key <= R[r].key:
                pairs[n] = L[l]
                l += 1
            else:
                pairs[n] = R[r]
                r += 1
            n += 1

        while l in range(len(L)):
            pairs[n] = L[l]
            l += 1
            n += 1
        while r in range(len(R)):
            pairs[n] = R[r]
            r += 1
            n += 1

