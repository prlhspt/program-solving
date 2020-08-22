import sys
read = sys.stdin.readline


def b_search(arr, target, left, right):
    if left > right:
        return 0
    middle = (left + right) // 2
    if arr[middle] == target:
        return 1
    elif arr[middle] > target:
        return b_search(arr, target, left, middle - 1)
    else:
        return b_search(arr, target, middle + 1, right)


N = int(read())
A = list(map(int, read().split()))
A.sort()

M = int(read())
B = list(map(int, read().split()))

left = 0
right = len(A) - 1

for B_ in B:
    out = b_search(A, B_, left, right)
    print(out)
