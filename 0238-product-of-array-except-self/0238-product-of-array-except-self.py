class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product_list, right_product_list = list(), list()
        left_product, right_product = 1, 1
        result = list()

        for i in range(len(nums)):
            if i == 0:
                left_product_list.append(left_product)
            else:
                left_product *= nums[i - 1]
                left_product_list.append(left_product)
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_product_list.append(right_product)
            else: 
                right_product *= nums[i + 1]
                right_product_list.append(right_product)
        right_product_list.reverse()
        
        for i in range(len(nums)):
            result.append(left_product_list[i] * right_product_list[i])

        return result