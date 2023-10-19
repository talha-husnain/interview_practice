class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first_length  = len(s)
        second_length = len(t)
        if first_length== second_length:
            sort_first = sorted(s)
            sort_second = sorted(t)
            if  sort_first == sort_second:
                return True
        return False


        