class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if res[-1][1] < interval[0]:
                    res.append(interval)
                else:
                    oldInterval = res.pop()
                    res.append([min(oldInterval[0], interval[0]), max(oldInterval[1], interval[1])])

        return res