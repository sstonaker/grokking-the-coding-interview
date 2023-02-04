"""
Problem Challenge 2: String Anagrams (hard)

Problem Statement

Given a string and a pattern, find all anagrams of the pattern in the given
string.

Every anagram is a permutation of a string. As we know, when we are not allowed
to repeat characters while finding permutations of a string, we get N!N!
permutations (or anagrams) of a string having NN characters. For example, here
are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the
pattern in the given string.

Example 1:


Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and
"qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca",
"cab", and "abc".
"""


def find_string_anagrams(string, pattern):
    start, match = 0, 0
    matches = []
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
                match += 1

        if match == len(m):
            matches.append(start)

        if end >= len(m) - 1:
            left = string[start]
            start += 1
            if left in m:
                if m[left] == 0:
                    match -= 1
                m[left] += 1

    return matches


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
