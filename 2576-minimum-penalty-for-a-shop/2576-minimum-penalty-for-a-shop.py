class Solution:
    def bestClosingTime(self, customers: str) -> int:
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