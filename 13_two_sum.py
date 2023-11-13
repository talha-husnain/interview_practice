class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check_set = {}
        for i, num in enumerate(nums):
            req = target-num
            if req in check_set:
                return [check_set[req], i]
            check_set[num] = i


# def twoSum(nums, target):
#     length = len(nums)
#     left = 0
#     right = length-1
#     nums_arr = sorted(nums)
#     while left < right:
#         c_s = nums_arr[left]+nums_arr[right]
#         if (c_s == target):
#             return (nums[left], nums[right])
#         elif (c_s > target):
#             right -= 1
#         elif (c_s < target):
#             left += 1


# result = twoSum([-1, -2, -3, 4, 5, 6, 7, 8], 9)
# print(result)
