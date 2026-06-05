class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic descreasing stack
        # as poping the elements calculate the distance 

        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # check if stack is empty 
            if not stack:
                stack.append(i)
                continue
            
            # if stack is not empty,
            # ensure monotonic decreasing property of the stack
            # as poping, calculate the distance and insert into result
            while stack and temperatures[i] > temperatures[stack[-1]]:
                distance = i - stack[-1]
                result[stack[-1]] = distance
                stack.pop()
            
            stack.append(i)

        return result
        