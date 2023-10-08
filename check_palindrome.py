# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         alphanumeric_chars = [char.lower() for char in s if char.isalnum()]
#     # Join the alphanumeric characters back into a string
#         cleaned_string = ''.join(alphanumeric_chars)
#         le =len(cleaned_string)
#         for i in range(le):
#             if s == " " :
#                 return True
#             elif cleaned_string[i] ==cleaned_string[le-1-i]:
#                 continue
#             else:
#                 return False
#         return True
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert all characters to lowercase and filter out non-alphanumeric characters
        alphanumeric_chars = [char.lower() for char in s if char.isalnum()]
        # Join the alphanumeric characters back into a string
        cleaned_string = ''.join(alphanumeric_chars)
        # If the cleaned string is empty or is equal to its reverse, then it's a palindrome
        return cleaned_string == cleaned_string[::-1]


        