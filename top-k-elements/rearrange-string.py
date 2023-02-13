"""Problem Statement

Given a string, find if its letters can be rearranged in such a way that no two
same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each
other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together
e.g., "apaa", "paaa".
"""

from heapq import heappop, heappush


def rearrange_string(string):
    char_frequency_map = {}
    for char in string:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

    max_heap = []
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    previous_char, previous_frequency = None, 0
    result_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        if previous_char and -previous_frequency > 0:
            heappush(max_heap, (previous_frequency, previous_char))
        result_string.append(char)
        previous_char = char
        previous_frequency = frequency + 1

    return ''.join(result_string) if len(result_string) == len(string) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
