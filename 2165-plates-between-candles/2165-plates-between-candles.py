class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * n
        left = [-1] * n
        right = [-1] * n

        plat_count = 0
        for i in range(n):
            if s[i] == '*':
                plat_count += 1
            prefix[i] = plat_count
        
        prev_candle = -1 
        for i in range(n):
            if s[i] == '|':
                prev_candle = i
            left[i] = prev_candle
        
        next_candle = -1 
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                next_candle = i
            right[i] = next_candle

        ans = []
        for l, r in queries:
            l_candle = right[l]
            r_candle = left[r]

            if l_candle != -1 and r_candle != -1 and l_candle < r_candle:
                count = prefix[r_candle] - prefix[l_candle]
                ans.append(count)
            else:
                ans.append(0)
        
        return ans