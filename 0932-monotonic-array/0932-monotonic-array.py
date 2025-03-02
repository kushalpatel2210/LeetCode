class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sortedAsc, sortedDesc = sorted(nums), sorted(nums, reverse = True)
        return True if nums == sortedAsc or nums == sortedDesc else False