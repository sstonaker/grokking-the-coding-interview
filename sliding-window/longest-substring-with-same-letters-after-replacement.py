"""Problem Statement

Given a string with lowercase letters only, if you are allowed to replace no
more than `k` letters with any letter, find the length of the longest substring
having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring
"bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring
"bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating
substring "ccc"."""


def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # try to extend the window size
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1

        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])

        # if remaining chars are less than k, shrink the window
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
