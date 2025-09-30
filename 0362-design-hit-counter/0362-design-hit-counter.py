import bisect

class HitCounter:

    def __init__(self):
        self.counts = list()
        self.timestamps = list()

    def hit(self, timestamp: int) -> None:
        if self.timestamps and self.timestamps[-1] == timestamp:
            self.counts[-1] += 1
        else:
            self.timestamps.append(timestamp)
            self.counts.append(1)

    def getHits(self, timestamp: int) -> int:
        start_window = timestamp - 300 + 1
        index = bisect.bisect_left(self.timestamps, start_window)
        return sum(self.counts[index:])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)