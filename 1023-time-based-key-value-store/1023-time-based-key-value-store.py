from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashMap[key]) - 1 
        diff = float('inf')
        element = ""

        while l <= r:
            m = l + (r - l) // 2
            val, time = self.hashMap[key][m]
            
            if time <= timestamp and timestamp - time < diff:
                element = val
            
            if time < timestamp:
                l = m + 1
            else:
                r = m - 1

        return element
        
'''
from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1
        
        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""

'''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)