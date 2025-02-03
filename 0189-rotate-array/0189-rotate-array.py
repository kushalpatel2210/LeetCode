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
