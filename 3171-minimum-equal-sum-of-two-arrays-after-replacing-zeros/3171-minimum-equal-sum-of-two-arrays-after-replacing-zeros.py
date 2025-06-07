class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1, zero2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1) + zero1, sum(nums2) + zero2
        
        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1
        
        return max(sum1, sum2)