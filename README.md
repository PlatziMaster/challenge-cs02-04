# PS04: Finding the partition

We define a partition **i** on an array **A** as the array where for all indices **j<i**,
**A[j] <= A[i]** and for all indices **k>i**, **A[k] > A[i]**. Given an array **A** modify it such that a partition was applied on **A[0]** (first element).

**Example 1:**
* Input: `[4,2,8,1,3,9]`
* Output: `None`
* Explanation: After running `partition(A)` on the input, A was modified to obtain `[2, 1, 3, 4, 8, 9]`. Notice that all elements before index **3** are less than or equal to **4** and all elements after index **3** are greater than **4**.

**Example 2:**
* Input: `[4, 9, 3, 6, 1]`
* Output: `None`
* Explanation: After running `partition(A)` on the input, A was modified to obtain `[3, 1, 4, 9, 6]`. Notice that all elements before index **2** are less than or equal to **4** and all elements after index **2** are greater than **4**.

**Note:** If this were the partition scheme used in a quicksort implementation, it will be expected that its time complexity is `O(n)` and space complexity is `O(1)`. It might also be expected to be an [stable partition](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability). This exercise only requires you to comply with the time and space complexities. Designing a stable algorithm is a plus.

**Details**:
* All elements of **A** are unique.
* 0 < `len(A)` < 10^7.

# How to submit.

* Complete the function `partition(A: List[int]):` under `solution.py`.
* All code will be checked for readability using [**pylint**](https://www.pylint.org/).
* A grader is included, and all test cases must pass.
* *Don't modify the grader!*

# Debugging

* You can run the grader with the command `python3 grader.py N` where `N` is the number of elements you want to test for.
