from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = r = 0
        max_length = 0
        max_count = 0
        char_count = defaultdict(int)

        while r < len(s):
            char = s[r]
            char_count[char] += 1
            max_count = max(max_count, char_count[char])

            if (r - l + 1 - max_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length
