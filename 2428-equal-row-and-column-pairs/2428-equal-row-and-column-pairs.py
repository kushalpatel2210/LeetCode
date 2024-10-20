from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        rows = [tuple(lst) for lst in grid]
        columns = [tupl for tupl in zip(*grid)]
        rows_counter, columns_counter = Counter(rows), Counter(columns)
        print(columns_counter)
    
        for key in rows_counter.keys():
            if key in columns_counter:
                count += rows_counter.get(key)* columns_counter.get(key)
        
        return count