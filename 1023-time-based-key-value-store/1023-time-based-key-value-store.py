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
        # print(f"l {l} r {r}")
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
        # if key in self.hashMap:
           
        # else:
        #     return ""
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)