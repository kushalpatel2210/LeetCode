class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_length = i + 1 
            right_length = len(nums) - i - 1

            if 2 * left[nums[i]] > left_length and 2 * right[nums[i]] > right_length:
                return i
        
        return -1