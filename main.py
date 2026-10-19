"""Three simple algorithms and a command line demonstration."""

import argparse


def bubble_sort(numbers):
    """Return a sorted copy of numbers in ascending order."""
    result = list(numbers)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def linear_search(numbers, target):
    """Return the first index of target, or -1 if it is absent."""
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def binary_search(sorted_numbers, target):
    """Return an index of target in an ascending list, or -1 if absent."""
    left, right = 0, len(sorted_numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_numbers[middle] == target:
            return middle
        if sorted_numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def main(argv=None):
    parser = argparse.ArgumentParser(description="演示冒泡排序和二分查找")
    parser.add_argument("numbers", nargs="+", type=int, help="要排序的整数")
    parser.add_argument("--target", type=int, help="要查找的整数")
    args = parser.parse_args(argv)

    sorted_numbers = bubble_sort(args.numbers)
    print("排序结果：{}".format(sorted_numbers))
    if args.target is not None:
        index = binary_search(sorted_numbers, args.target)
        if index == -1:
            print("没有找到 {}。".format(args.target))
        else:
            print("{} 位于排序结果的第 {} 个位置（从 0 开始）。".format(args.target, index))


if __name__ == "__main__":
    main()
