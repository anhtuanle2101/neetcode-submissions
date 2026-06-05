class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(timestamp, value)]
            return
        
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        arr = self.m.get(key, [])

        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
    
        
            
        
