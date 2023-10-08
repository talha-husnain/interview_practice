class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to store opening brackets
        stack = []
        # For each character in the string
        for char in s:
            # If it's an opening bracket, push onto the stack
            if char in "({[":
                stack.append(char)
            # If it's a closing bracket
            else:
                # If the stack is empty, return False
                if not stack:
                    return False
                # If the stack is not empty, pop the top and check for a match
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        # After processing all characters, return True if stack is empty
        return len(stack) == 0
