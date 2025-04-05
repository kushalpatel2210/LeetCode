# Top Down DP
class Solution:
    def fib(self, n: int) -> int:
        memo = {0 : 0, 1 : 1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
                return memo[x]
        
        return f(n)
        

'''
# Noraml Solution
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
'''