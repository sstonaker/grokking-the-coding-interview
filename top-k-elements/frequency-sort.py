"""Problem Statement

Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before
any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared
only once."""


from heapq import heappop, heappush


def sort_character_by_frequency(string):
    char_frequency_map = {}
    for char in string:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1
    max_heap = []
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    sorted_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        for _ in range(-frequency):
            sorted_string.append(char)

    return ''.join(sorted_string)


def main():

    print(
        f"String after sorting characters by frequency: {sort_character_by_frequency('Programming')}")
    print(
        f"String after sorting characters by frequency: {sort_character_by_frequency('abcbab')}")


main()
