class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for i in range(len(pairs)):
            p, s = pairs[i]
            stack.append((target - p) / s) # time for current car get to destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # there is at least two cars and the last car is slower than 
                # the previous car, they will be come one fleet
                stack.pop()
        
        return len(stack)

        

        