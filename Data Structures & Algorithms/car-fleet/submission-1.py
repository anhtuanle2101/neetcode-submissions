class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # sorting the car's location
        # as we are checking each car backwards
        # if the car arrives ealier than the last 
        # car in the stack which means they can be grouped
        # into a car fleet, we can ignore this car
        # otherwise, add the car into the stack

        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort()
        stack = []
        for car in cars:
            pos, speed = car
            time = (target-pos) / speed
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)

