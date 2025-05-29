# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityElement = None

        for num in nums:
            if not count:
                majorityElement = num
            count += (1 if num == majorityElement else -1) 
        
        return majorityElement
