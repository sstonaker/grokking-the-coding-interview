"""Problem Statement

For `K` employees, we are given a list of intervals representing each
employee`s working hours. Our goal is to determine if there is a free interval
which is common to all employees. You can assume that each list of employee
working hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].
Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].
Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7]."""


from heapq import heappop, heappush


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval  # interval representing working hours
        # list containing hours of this employee
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, min_heap = [], []

    # insert first interval of each employee into the queue
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    previous_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)
        # if previous interval is not overlapping, insert a free interval
        if previous_interval.end < queue_top.interval.start:
            result.append(Interval(previous_interval.end,
                          queue_top.interval.start))
            previous_interval = queue_top.interval
        else:  # overlapping intervals - update the previous interval
            if previous_interval.end < queue_top.interval.end:
                previous_interval = queue_top.interval

        # if there are more intervals for the same employee, add next interval
        employee_schedule = schedule[queue_top.employee_index]
        if len(employee_schedule) > queue_top.interval_index + 1:
            heappush(min_heap, EmployeeInterval(
                employee_schedule[queue_top.interval_index + 1],
                queue_top.employee_index, queue_top.interval_index + 1))

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
