from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            values = self.map[key]
            for i in range(len(values) - 1, -1 , -1):
                if values[i][1] <= timestamp:
                    return values[i][0]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)