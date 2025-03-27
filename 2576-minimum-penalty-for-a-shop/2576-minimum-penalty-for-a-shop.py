class Solution:
    def bestClosingTime(self, customers: str) -> int:
        no_of_y = customers.count('Y')
        no_of_n = 0
        penalty = no_of_y
        res = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                no_of_y -= 1
            else:
                no_of_n += 1

            curr_penalty = no_of_y + no_of_n
            
            if curr_penalty < penalty:
                res = i + 1
                penalty = curr_penalty

        return res