from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key]) - 1
        element = ""
        diff = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            val, time = self.map[key][mid]
            
            if time <= timestamp:
                element = val
                l = mid + 1
            else:
                r = mid - 1
        
        return element

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)