class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) > 1 and stack[-1] < 0 and stack[-2] >= 0:
                pop1 = stack.pop()
                pop2 = stack.pop()

                if abs(pop1) > abs(pop2):
                    stack.append(pop1)
                elif abs(pop1) < abs(pop2):
                    stack.append(pop2)

        return stack