class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# My way


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_num = 1
        li = []
        if len(s) == 0:
            max_num = 0
        for i in range(len(s)-2):

            if s[i] != s[i+1] and s[i] not in li:
                li.append(s[i])
                count += 1
                max_num = max(max_num, count)
            else:
                count = 1

        return max_num
