class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_dic = set()
        for num in nums:
            if num in set_dic:
                return True
            else:
                set_dic.add(num)
        return False 
        