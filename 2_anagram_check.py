class Solution(object):
    def isAnagram(self, s, t):
        first_length = len(s)
        second_length = len(t)
        if first_length == second_length:
            sort_first = sorted(s)
            sort_second = sorted(t)
            if sort_first == sort_second:
                return True
        return False


def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)
