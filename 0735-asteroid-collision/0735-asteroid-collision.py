class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            if stack and stack [-1] >= 0 and asteroids[i] < 0:
                stack.append(asteroids[i])
                while len(stack) > 1 and stack[-2] >= 0 and stack[-1] < 0: 
                    if abs(stack[-1]) > abs(stack[-2]):
                        first = stack.pop()
                        second = stack.pop()
                        stack.append(first)
                        print(stack)
                    elif abs(stack[-1]) == abs(stack[-2]):
                        stack.pop()
                        stack.pop()
                    else:
                        stack.pop()
                        break
            else:
                stack.append(asteroids[i])
        
        return stack