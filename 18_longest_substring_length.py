class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        max_count = 0
        left = 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_count = max(max_count, right-left + 1)

        return max_count if s else 0

        # count = 0
        # max_num = 1
        # li = []
        # if len(s) ==0:
        #     max_num = 0
        # for i in range(len(s)-1):

        #     if s[i]!= s[i+1] and s[i] not in li:
        #         li.append(s[i])
        #         count +=1
        #         max_num = max(max_num, count)
        #     else:
        #         count =1

        # return max_num
