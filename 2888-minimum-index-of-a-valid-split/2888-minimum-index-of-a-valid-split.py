class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        most_common = counter.most_common(1)[0][0]
        left = 0
        right = counter.most_common(1)[0][1]
        
        for i in range(len(nums)):
            if nums[i] == most_common:
                left += 1
                right -= 1
            
                left_size = i + 1
                right_size = len(nums) - i - 1

                if 2 * left > left_size and 2 * right > right_size:
                    return i
        
        return -1



'''
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
'''