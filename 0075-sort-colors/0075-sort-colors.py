class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptrVal = 0
        i = 0

        while i < len(nums) and ptrVal < 3:
            print(f"i {i} nums[i] {nums[i]} ptrVal {ptrVal}")
            currVal = nums[i]
            j = i + 1
            if nums[i] == ptrVal:
                i += 1
            
            while j < len(nums) - 1 and nums[j] != ptrVal:
                j += 1
            
            if j < len(nums) and nums[j] == ptrVal:
                print(f"j {j} nums[j] {nums[j]}")
                nums[i], nums[j] = nums[j], nums[i]
            else:
                print(f"j {j}")
                ptrVal += 1
                continue
            print(f"ptrVal {ptrVal}")
            print(f"nums {nums}")
            print("-------------")
            i += 1
        

            