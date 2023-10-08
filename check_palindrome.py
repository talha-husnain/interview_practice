class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alphanumeric_chars = [char.lower() for char in s if char.isalnum()]
    # Join the alphanumeric characters back into a string
        cleaned_string = ''.join(alphanumeric_chars)
        le =len(cleaned_string)
        for i in range(le):
            if s == " " :
                return True

            elif cleaned_string[i] ==cleaned_string[le-1-i]:
                continue
            else:
                return False
        return True

        