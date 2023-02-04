"""
Given a string and a pattern, find out if the string contains any permutation
of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For
example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given
pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a
substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given
pattern.
"""


def find_permutation(string, pattern):
    start, matched = 0, 0
    m = {}

    for p in pattern:
        if p not in m:
            m[p] = 0
        m[p] += 1

    for end in range(len(string)):
        right = string[end]

        if right in m:
            m[right] -= 1
            if m[right] == 0:
                matched += 1

        if matched == len(m):
            return True

        if end >= len(pattern) - 1:
            left = string[start]
            start += 1
            if left in m:
                if m[left] == 0:
                    matched -= 1
                m[left] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy",
                                                       "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
