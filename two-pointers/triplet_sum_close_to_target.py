"""Given an array of unsorted numbers and a target number, find a triplet in
the array whose sum is as close to the target number as possible, return the
sum of the triplet. If there are more than one such triplet, return the sum of
the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
Example 4:

Input: [0, 0, 1, 1, 2, 6], target=5
Output: 4
Explanation: There are two triplets with distance '1' from target: [1, 1, 2]
& [0,0, 6]. Between these two triplets, the correct answer will be [1, 1, 2]
as it has a sum '4' which is less than the sum of the other triplet which is
'6'. This is because of the following requirement: 'If there are more than one
such triplet, return the sum of the triplet with the smallest sum.'"""

import math


def triplet_sum_close_to_target(arr, target):
    arr.sort()
    smallest = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # found an exact sum
                return target

            # the second part of the following 'if' is to handle the smallest
            # sum when we have more than one solution
            if (
                abs(target_diff) < abs(smallest)
                or (abs(target_diff) == abs(smallest))
                and target_diff > smallest
            ):
                smallest = target_diff  # save the closest / biggest difference

            if target_diff > 0:
                left += 1  # need a bigger sum
            else:
                right -= 1  # need a smaller sum

    return target - smallest


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))


main()
