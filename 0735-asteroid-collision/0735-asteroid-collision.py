class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            stack.append(a)
            
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                first, second = stack.pop(), stack.pop()   
             
                if abs(first) > abs(second):
                    stack.append(first)
                elif abs(second) > abs(first):
                    stack.append(second)
        
        return stack