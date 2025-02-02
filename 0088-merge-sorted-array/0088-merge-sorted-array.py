class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_m, index_n = m - 1, n - 1
        ptr = m + n - 1

        while index_n >= 0:
            if index_m >= 0 and nums1[index_m] >= nums2[index_n]:
                nums1[ptr] = nums1[index_m]
                index_m -= 1 
            else:
                nums1[ptr] = nums2[index_n]
                index_n -= 1
            ptr -= 1