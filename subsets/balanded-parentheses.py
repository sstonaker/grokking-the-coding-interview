"""Problem Statement

For a given number `N`, write a function to generate all combination of `N`
pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()"""

from collections import deque


class ParenthesesString:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(ParenthesesString(
                    ps.str + "(", ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:
                queue.append(ParenthesesString(ps.str + ")",
                             ps.open_count, ps.close_count + 1))
    return result


def main():
    print(
        f"All combinations of balanced parentheses are: {str(generate_valid_parentheses(2))}")
    print(
        f"All combinations of balanced parentheses are: {str(generate_valid_parentheses(3))}")


main()
