def length_of_longest_substring(s):
    char_index_map = {}
    max_length = start = 0

    for end in range(len(s)):
        if s[end] in char_index_map:
            # Update the start of the window if the repeating character is inside the current window
            start = max(start, char_index_map[s[end]] + 1)
        char_index_map[s[end]] = end  # Update the last index of characters
        max_length = max(max_length, end - start + 1)

    return max_length


def min_subarray_len(s, nums):
    min_length = float('inf')
    window_sum = start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum >= s:
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0


def longest_substring_with_k_distinct(s, k):
    if not s:
        return 0

    char_map = {}  # To store the frequency of characters in the current window
    max_length = start = 0

    for end in range(len(s)):
        right_char = s[end]
        char_map[right_char] = char_map.get(right_char, 0) + 1

        # Shrink the window if we have more than k distinct characters
        while len(char_map) > k:
            left_char = s[start]
            char_map[left_char] -= 1
            if char_map[left_char] == 0:
                del char_map[left_char]
            start += 1  # Shrink the window

        # Update the max length of the substring found so far
        max_length = max(max_length, end - start + 1)

    return max_length
