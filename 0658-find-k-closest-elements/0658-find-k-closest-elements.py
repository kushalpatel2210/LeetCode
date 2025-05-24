class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = list()

        for num in arr:
            diffs.append(abs(num - x))
        
        print(diffs)
        
        i = 0
        currSum, minSum = 0, float('inf')
        idx = float('inf')
        for j in range(len(diffs)):
            currSum += diffs[j]

            if j - i + 1 < k:
                continue

            # print(currSum, minSum)

            if currSum < minSum:
                minSum = currSum
                idx = i
            
            currSum -= diffs[i]
            i += 1

        return arr[idx:idx + k]
            