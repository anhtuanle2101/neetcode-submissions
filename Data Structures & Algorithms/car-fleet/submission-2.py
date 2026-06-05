'''
    position[i] starting pos of ith car
    speed[i] speed of ith car (distance/time) -> slope of 2d graphs distance by time 
    target is a pos for the cars to reach

    - no passing
        - if a faster car reached another car -> two cars become one fleet and drive at slower speed
    - a single car can be one fleet
    - catch at the target pos will also become a part of the fleet

    - sort the (pos, speed) list
    - monotonic stack (decreasing)
        - at ith car 
            - pop every car that reach the target faster (top_time <= time[i]) current car (since they will be come one fleet and moving together)
            - push the value into the stack

'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = [(pos, sp, (target-pos)/sp) for pos, sp in zip(position, speed)]
        sorted_list.sort()
        stack = []
        for i in range(len(sorted_list)):
            while stack and sorted_list[i][2] >= stack[-1][2]: # remove each car moving faster than current car of the stack
                stack.pop()
            # all faster car will be become one fleet with the current car 
            stack.append(sorted_list[i])
    
        return len(stack)