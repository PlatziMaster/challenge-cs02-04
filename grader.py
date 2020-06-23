"""PS04 Grader."""

import argparse
import copy
import random
import sys

from solution import Solution


random.seed(0)


def generate_test_case(n): # pylint: disable=C0103
    """Return test case of size n and first value of test case."""
    data = set()
    while len(data) < n:
        data.add(random.randint(0, n*3))
    data = list(data)
    random.shuffle(data)
    return data, data[0]


def is_valid_output(output, pivot_value):
    """Verify solution correctness."""
    pivot_index = 0
    try:
        pivot_index = output.index(pivot_value)
    except ValueError:
        return False

    for i, value in enumerate(output):
        if i < pivot_index and value > pivot_value:
            return False
        if i > pivot_index and value < pivot_value:
            return False

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PS04 argument parser.')
    parser.add_argument('n', type=int, help='test case size')
    args = parser.parse_args()

    test_case, pivot = generate_test_case(args.n)
    original_input = copy.copy(test_case)
    sol = Solution()
    sol.partition(test_case)
    if not is_valid_output(test_case, pivot):
        print(f"\t❌ Test case failed (n={args.n})")
        if args.n < 100:
            print("\t\tInput:", original_input)
            print("\t\tGot:", test_case)
        sys.exit(1)
    print(f"\t✅ Test case accepted (n={args.n})")
