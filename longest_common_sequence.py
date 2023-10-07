class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        leng =1
        numbers  = sorted(nums)
        for i in range(0,n-1):
            if numbers[i] - numbers[i+1] == 1 or numbers[i] - numbers[i+1] == -1:
                leng +=1
            else:
                leng = leng
        return leng

        