'''
    Storing multiple values for the same key at specified time stamps
    Retrieving the key's value at a specified timestamp     

    set Stores the key key with the value value at the given time timestamp.
    store[key].append((timestamp, value))

    get Returns the most recent value of key if set was previously called on it 
    and the most recent timestamp for that key 
    prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). 
    If there are no values, it returns ""
    - look for the value to return
        - the timestamp_target <= timestamp_input -> return left
        - binary search the timestamp_target
            - if middle timestamp > target -> look into left of the middle
            - if mdidle timestamp < target -> look into right of the middle 
       
    [1, 2, 5, 10]
    the timestamps are in strictly increasing order for set calls -> timestamps will be also strictly 
    increasing for the same key in the store
'''

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
            return

        self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # get the list of values sorted by timestamps
        if key not in self.store:
            return ""
        res = ""
        ts_and_v = self.store[key]
        left, right = 0, len(ts_and_v) - 1

        while left <= right:
            middle = left + (right-left)//2
            middle_ts = ts_and_v[middle][0]
            # if middle_ts == timestamp:
            #     return ts_and_v[middle][1]
            if middle_ts > timestamp:
                right = middle - 1
            else:
                res = ts_and_v[middle][1]
                left = middle + 1
        
        return res

        
