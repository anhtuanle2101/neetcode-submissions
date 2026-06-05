'''
    temperatutes[i] ith day temp
    
    result[i] is number of days after ith day in temperatures which a higher temp than temperatures[i] if there is no higher temperatures in future
    result[i] = 0

    result = [0] * len(temperatures)
    - monotonic stack
        - if there is a new value, before pushing the value into the stack
            - pop all elements <= the current value
            - then push the value into the stack
    - at ith day, if any temparatures in stack is less than temperatures[i] should be popped out since this will be the first warmer temperature,
        -> calculate the distance and update the result list res[pop_idx] = (i - pop_idx)
        - push the value (index, temperatures[i]) to the stack afterwards
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while monotonic_stack and temperatures[i] > monotonic_stack[-1][1]:    
                top = monotonic_stack.pop()
                pop_idx, pop_value = top
                res[pop_idx] = i - pop_idx

            monotonic_stack.append((i, temperatures[i]))

        return res