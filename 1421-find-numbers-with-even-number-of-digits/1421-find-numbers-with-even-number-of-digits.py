class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenDigits = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                evenDigits += 1
        
        return evenDigits