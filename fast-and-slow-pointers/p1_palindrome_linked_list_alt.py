"""Problem Statement

Given the head of a Singly LinkedList, write a method to check if the
LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in
the original form once the algorithm is finished. The algorithm should have
O(N) time complexity where `N` is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false"""

import copy


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_end(head):
    current = head
    while current.next is not None:
        current = current.next
    return current


def check_palindrome(head):
    left = head
    reversed_list_copy = copy.deepcopy(head)
    reversed_list = reverse(reversed_list_copy)
    right = reversed_list

    while left.next is not None:
        if (left.value != right.value):  # type: ignore
            return False
        left = left.next
        right = right.next  # type: ignore
    return True


def reverse(head):
    prev = None
    while (head is not None):
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
    return prev


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.value)
        cur = cur.next


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(check_palindrome(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(check_palindrome(head)))


main()
