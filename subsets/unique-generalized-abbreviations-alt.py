"""Problem Statement

Given a word, write a function to generate all of its unique generalized
abbreviations.

A generalized abbreviation of a word can be generated by replacing each
substring of the word with the count of characters in the substring. Take the
example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After
replacing these substrings in the actual word by the count of characters,
we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.

Note: All contiguous characters should be considered one substring, e.g., we
can’t take “a” and “b” as substrings to get “11”; since “a” and “b” are
contiguous, we should consider them together as one substring to get an
abbreviation “2”.

Example 1:

Input: "BAT"
Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
Example 2:

Input: "code"
Output: "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode"
, "1od1", "1o1e", "1o2",
"2de", "2d1", "3e", "4"
"""


def generate_generalized_abbreviation(word):
    result = []
    generate_abbreviation_recursive(word, list(), 0, 0, result)
    return result


def generate_abbreviation_recursive(word, abWord, start, count, result):

    if start == len(word):
        if count != 0:
            abWord.append(str(count))
        result.append(''.join(abWord))
    else:
        # continue abbreviating by incrementing the current abbreviation count
        generate_abbreviation_recursive(
            word, list(abWord), start + 1, count + 1, result)

        # restart abbreviating, append the count and the current character to the string
        if count != 0:
            abWord.append(str(count))
        newWord = list(abWord)
        newWord.append(word[start])
        generate_abbreviation_recursive(word, newWord, start + 1, 0, result)


def main():
    print(
        f"Generalized abbreviation are: {str(generate_generalized_abbreviation('BAT'))}")
    print(
        f"Generalized abbreviation are: {str(generate_generalized_abbreviation('code'))}")


main()
