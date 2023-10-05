class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Create a dictionary to store the frequency of each element
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Sort the dictionary by values in descending order
        sorted_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        
        # Get the top k elements from the sorted dictionary
        result = [key for key, _ in sorted_dict[:k]]
        
        return result
