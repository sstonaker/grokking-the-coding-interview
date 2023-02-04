"""
Problem Challenge 4: Words Concatenation (hard)

Problem Statement

Given a string and a list of words, find all the starting indices of substrings
in the given string that are a concatenation of all the given words exactly
once without any overlapping of words. It is given that all words are of the
same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" &
"foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""


def word_concat(string, words):

    if len(words) == 0 or len(words[0]) == 0:
        return []

    m = {}

    for word in words:
        if word not in m:
            m[word] = 0
        m[word] += 1

    result = []
    n_words = len(words)
    word_l = len(words[0])

    for i in range((len(string) - n_words * word_l) + 1):
        seen = {}
        for j in range(0, n_words):
            next_i = i + j * word_l
            word = string[next_i: next_i + word_l]
            if word not in m:
                break

            if word not in seen:
                seen[word] = 0
            seen[word] += 1

            if seen[word] > m.get(word, 0):
                break

            if j + 1 == n_words:
                result.append(i)

    return result


def main():
    print(word_concat("catfoxcat", ["cat", "fox"]))
    print(word_concat("catcatfoxfox", ["cat", "fox"]))


main()
