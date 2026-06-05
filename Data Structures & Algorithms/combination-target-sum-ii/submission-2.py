'''
    candidates int[]
    - possible duplicates
    target int
    OUT: no duplicate subsets of candidates where sum(candidates) = target
    - order not matter
    - backtrack with sorted candidates [1,1,2,3] target = 5
        - at ith candidate
            - total sum = target:
                valid subset
            - stop condition
                i >= len(candidates) or total > target
            - distinct options
                - include the number at candidates[i] 
                - not include the number at candidates[i]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.cur = []
        self.candidates = candidates
        self.candidates.sort()

        self.target = target

        self.backtrack(0, 0)

        return self.result


    def backtrack(self, i, total):
        if total == self.target:
            self.result.append(self.cur[:])
            return

        if i >= len(self.candidates) or total > self.target:
            return

        # choose ith candidate
        total += self.candidates[i]
        self.cur.append(self.candidates[i])

        # move forward
        self.backtrack(i + 1, total)

        # backtrack
        total -= self.candidates[i]
        self.cur.pop()

        # not choose the number at candidates[i], loop until get a different int
        while i + 1 < len(self.candidates) and self.candidates[i] == self.candidates[i + 1]:
            i += 1
        
        # move forward 
        self.backtrack(i + 1, total)
