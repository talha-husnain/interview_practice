class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check_set = {}
        for i,num in enumerate(nums):
            req = target-num
            if req in check_set:
                return [check_set[req],i]
            check_set[num] =i


        