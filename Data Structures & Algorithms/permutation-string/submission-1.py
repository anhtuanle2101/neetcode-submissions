'''
    use hash map to count the characters in s1, then loop through s2, 
    - at index i, get the substring [i, i + len(s1)] 
    make the comparison O(1) to do the comparison if it matches return True


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        left = 0
        s2_count = {}

        for right in range(len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            
            if right >= len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1
                
            if len(s2_count) == len(s1_count):
                identical = True
                for k in s2_count:
                    if k not in s1_count:
                        identical = False
                        break
                    if s2_count[k] != s1_count[k]:
                        identical = False
                        break
                if identical:
                    return True

        return False