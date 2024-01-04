class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:
            # Check if the number is the start of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

                # Keep checking next numbers in the sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                # Update the longest sequence found
                longest_sequence = max(longest_sequence, current_length)

        return longest_sequence
# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         leng =1
#         numbers  = sorted(nums)
#         for i in range(0,n-1):
#             if numbers[i] - numbers[i+1] == 1 or numbers[i] - numbers[i+1] == -1:
#                 leng +=1
#             else:
#                 leng = leng
#         return leng
