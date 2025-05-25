class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Monolithic decreasing stack

        for i, temp in enumerate(temperatures):            
            while stack and stack[-1][1] < temp:
                day, tempAtGivenDay = stack.pop()
                res[day] = i - day

            stack.append((i, temp))
            
        return res