from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage[key]
        l, r = 0, len(values) - 1
        res = ''

        while l <= r:
            m = l + (r - l) // 2
            valAtMid, timestampAtMid = values[m]

            if timestampAtMid <= timestamp:
                res = valAtMid
                l = m + 1
            else:
                r = m - 1
        
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)