class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        count_y = customers.count('Y')
        count_n = 0
        penalty = float('inf')
        closing_hour = 0

        for i in range(n + 1):
            curr_penalty = count_y + count_n
            if curr_penalty < penalty:
                penalty = curr_penalty
                closing_hour = i
            
            if i < n:
                if customers[i] == 'Y':
                    count_y -= 1
                if customers[i] == 'N':
                    count_n += 1
        
        return closing_hour