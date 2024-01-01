class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Initialize arrays
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i-1]
            left[i] = left_product
        # Calculate right products
        right_product = 1
        for i in range(n-2, -1, -1):
            right_product *= nums[i+1]
            right[i] = right_product

        # Compute final result by multiplying left and right products
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
