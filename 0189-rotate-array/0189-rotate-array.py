class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n -1)
        self.reverse(nums, 0, k -1)
        self.reverse(nums, k, n -1)

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        ans = [0] * len(nums)

        for i in range(len(nums)):
            index = ( i + k ) % n
            ans[index] = nums[i]
                
        nums[:] = ans
'''