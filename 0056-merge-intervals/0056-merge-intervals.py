class Solution:
    def isOverlapping(self, interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        return end - start >= 0

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        res = [intervals[0]]

        for interval in intervals:
            currInterval = res[-1]

            if self.isOverlapping(currInterval, interval):
                res[-1] = [min(interval[0], currInterval[0]), max(interval[1], currInterval[1])]
            else:
                res.append(interval)

        return res