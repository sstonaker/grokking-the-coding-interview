"""Problem Statement

Given an array of `K` sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]"""


from heapq import heappop, heappush


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minHeap = []

    # put the root of each list in the min heap
    for root in lists:
        if root is not None:
            heappush(minHeap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    resultHead, resultTail = None, None
    while minHeap:
        node = heappop(minHeap)
        if resultHead is None:
            resultHead = resultTail = node
        else:
            resultTail.next = node  # type: ignore
            resultTail = resultTail.next  # type: ignore

        if node.next is not None:
            heappush(minHeap, node.next)

    return resultHead


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
