# Cycle detection problem -> Floyd's algorithm
class Solution:
    def get_next_int(self, x) -> int:
        next_num = 0

        while x > 0:
            digit = x % 10

            x //= 10

            next_num += digit ** 2
        
        return next_num

    def isHappy(self, n: int) -> bool:
        slow = fast = n 

        while True:
            slow = self.get_next_int(slow)
            fast = self.get_next_int(self.get_next_int(fast))

            if fast == 1:
                return True
            elif fast == slow:
                return False