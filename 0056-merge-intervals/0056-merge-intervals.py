class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                lastEle = res.pop()
                if interval[0] > lastEle[1]:
                    res.append(lastEle)
                    res.append(interval)
                else:
                    newIntervalEnd = max(lastEle[1], interval[1])
                    res.append([lastEle[0], newIntervalEnd])

        return res