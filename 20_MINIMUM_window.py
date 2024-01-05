class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = r = 0
        counter = 0
        min_s = ""
        min_len = float('inf')  # Initialize with positive infinity

        while r < len(s):
            if s[r] in t:
                counter += 1

            while counter == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_s = s[l:r + 1]

                if s[l] in t:
                    counter -= 1

                l += 1

            r += 1

        return min_s
