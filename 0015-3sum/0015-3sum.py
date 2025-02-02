class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                diff = nums[l] + nums[r] + num

                if diff == 0:
                    triplets.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif diff > 0:
                    r -= 1
                else:
                    l += 1
         
        return [list(tpl) for tpl in triplets]