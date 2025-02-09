class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # temp, index

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, day = stack.pop()
                result[day] = i - day
            stack.append([t, i])

        return result 

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            diff = 0

            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > curr_temp:
                    diff = j - i
                    break
            
            result.append(diff)
        
        return result
'''