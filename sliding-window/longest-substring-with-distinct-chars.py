"""Problem Statement

Given a string, find the length of the longest substring, which has all
distinct characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde"."""


def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if map contains right char; shrink so there is only 1 right char
        if right_char in char_index_map:
            # we will not have any right char after its previous index
            # and if window start is ahead of last index, keep window start
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert right char into map
        char_index_map[right_char] = window_end
        # remember the max so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
