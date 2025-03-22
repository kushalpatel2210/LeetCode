class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num

        while start <= end:
            mid = start + (end - start) // 2
            midSquare = mid ** 2

            if midSquare == num:
                return True
            elif midSquare > num:
                end = mid - 1
            else:
                start = mid + 1
        
        return False