class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self, left_products, right_products = list(), list(), list()
        left_product = right_product = 1

        for index, value in enumerate(nums):
            if index == 0:
                left_products.append(left_product)
            else:
                left_product *= nums[index - 1]
                left_products.append(left_product)
        
        for index in range(len(nums) -1, -1, -1):
            if index == len(nums) - 1:
                right_products.append(1)
            else:
                right_product *= nums[index + 1]
                right_products.append(right_product)
        right_products.reverse()

        for i in range(len(nums)):
            product_except_self.append(left_products[i] * right_products[i])
        
        return product_except_self