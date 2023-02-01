"""Problem Statement

Given the head of a Singly LinkedList that contains a cycle, write a function
to find the starting node of the cycle."""


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


def find_start(head):
    cycle_length = find_cycle_length(head)
    slow, fast = head, head
    while cycle_length > 0:
        fast = fast.next
        cycle_length -= 1
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.value


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_start(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_start(head)))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_start(head)))


main()
