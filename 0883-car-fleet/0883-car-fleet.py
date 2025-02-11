class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)

            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
'''