class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        nums1_uncommon = nums1_set.difference(nums2_set)
        nums2_uncommon = nums2_set.difference(nums1_set)

        return [list(nums1_uncommon),list(nums2_uncommon)]
