class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = 0
        score = 0
        right_time = -1
        for i in range(len(customers)):
            score += 1 if customers[i] == 'Y' else -1
            if score > max_score:
                max_score = score
                right_time = i
        return right_time + 1

'''
        no_of_y = customers.count('Y')
        no_of_n = 0
        penalty = float('inf')
        res = 0

        for i in range(len(customers) + 1):
            curr_penalty = no_of_y + no_of_n
            
            if curr_penalty < penalty:
                res = i
                penalty = curr_penalty

            if i < len(customers):
                if customers[i] == 'Y':
                    no_of_y -= 1
                else:
                    no_of_n += 1
                
        return res
'''