"""Problem Statement

Given the head of a LinkedList with a cycle, find the length of the
cycle.

Example:
Following LinkedList has a cycle:
head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                  ^..............^

Following LinkedList doesn't have a cycle:
head -> 2 -> 4 -> 6 -> 8 -> 10 -> null
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found a cycle so begin counting
            count = 0
            count_pointer = head
            while (count_pointer != slow):
                count += 1
                count_pointer = count_pointer.next
            return count
    return 0  # no cycle


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
