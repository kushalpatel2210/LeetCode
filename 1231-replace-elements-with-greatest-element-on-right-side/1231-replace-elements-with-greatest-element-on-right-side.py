class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        res = [-1] * len(arr)
        maximum = arr[len(arr) - 1]

        for i in range(len(arr) - 2, -1, -1):
            res[i] = maximum
            if arr[i] > maximum:
                maximum = arr[i]
        
        return res