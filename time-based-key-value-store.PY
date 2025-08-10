# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".



from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        # for i in range(len(values)-1, -1, -1):
        #     if values[i][0] <= timestamp:
        #         return values[i][1]


        left = 0
        right = len(values) - 1
        res = ""
        while(left <= right):
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)