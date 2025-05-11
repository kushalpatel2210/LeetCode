class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = list()
        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                lastElement = res.pop()
                if interval[0] <= lastElement[1]:
                    end = max(lastElement[1], interval[1])
                    res.append([lastElement[0], end])
                else:
                    res.append(lastElement)
                    res.append(interval)

        return res