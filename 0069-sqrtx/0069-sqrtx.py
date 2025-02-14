class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0

        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x: 
                r = mid - 1
            else:
                l = mid + 1
                result = mid
        
        return result
        