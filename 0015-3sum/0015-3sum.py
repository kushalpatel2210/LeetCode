class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):
            current = nums[i]
            target = -current

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    result.add(tuple([current, nums[j], nums[k]]))
                    j += 1
                    k -= 1

        return [list(tpl) for tpl in result]
        