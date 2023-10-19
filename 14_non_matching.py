def non_matching_chars(s1: str, s2: str) -> str:
    return ''.join([char for char in s1 if char not in s2])
