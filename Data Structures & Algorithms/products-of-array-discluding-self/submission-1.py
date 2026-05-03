class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        product_hash = [1] * size

        left_product = 1
        for i in range(size):
            product_hash[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(size-1, 0, -1):
            right_product *= nums[i]
            product_hash[i-1] = product_hash[i-1] * right_product
        
        return product_hash