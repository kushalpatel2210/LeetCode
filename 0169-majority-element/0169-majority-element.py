class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityElement = None

        for num in nums:
            if not count:
                majorityElement = num
                count += 1
            elif num == majorityElement:
                count += 1
            else:
                count -= 1
        
        return majorityElement
