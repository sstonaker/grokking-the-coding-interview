"""
Problem Statement

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern
"""


def find_substring(string, pattern):
    start, match, ss = 0, 0, 0
    min_l = len(string) + 1
    m = {}

    for p in pattern:
        if p not in m:
            m[p] = 0
        m[p] += 1

    for end in range(len(string)):
        right = string[end]

        if right in m:
            m[right] -= 1
            if m[right] >= 0:
                match += 1

        while match == len(pattern):
            if min_l > end - start + 1:
                min_l = end - start + 1
                ss = start

            left = string[start]
            start += 1

            if left in m:
                if m[left] == 0:
                    match -= 1
                m[left] += 1

    if min_l > len(string):
        return ""

    return string[ss:ss+min_l]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()
