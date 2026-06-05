

class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        self.min_value = float("-inf")        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val < self.min_st[-1]:
            self.min_value = val
        else:
            self.min_value = self.min_st[-1]

        self.min_st.append(self.min_value)

    def pop(self) -> None:
        if self.st:
            self.st.pop()
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
        
