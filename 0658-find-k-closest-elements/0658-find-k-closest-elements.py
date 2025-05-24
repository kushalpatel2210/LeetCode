class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointer
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:
            if abs(arr[r] - x) >= abs(arr[l] - x):
                r -= 1
            else:
                l += 1
        
        return arr[l : r + 1]

'''
# Sliding Window

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = list()

        for num in arr:
            diffs.append(abs(num - x))
                
        i = 0
        currSum, minSum = 0, float('inf')
        idx = float('inf')
        for j in range(len(diffs)):
            currSum += diffs[j]

            if j - i + 1 < k:
                continue

            if currSum < minSum:
                minSum = currSum
                idx = i
            
            currSum -= diffs[i]
            i += 1

        return arr[idx:idx + k]
'''