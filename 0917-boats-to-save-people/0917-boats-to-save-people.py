class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n -1
        count = 0

        while l <= r:
            remainingCap = limit - people[r]
            r -= 1
            count += 1

            if l <= r and people[l] <= remainingCap:
                l += 1
        
        return count

'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        l, r = 0, n - 1 
        count = 0
        people.sort()

        while l <= r:
            if l == r:
                count += 1
                return count
            elif (people[l] + people[r]) <= limit:
                l += 1 
                r -= 1
            elif people[r] <= limit:
                r -= 1
            else:
                l += 1

            count += 1       
             
        return count
'''