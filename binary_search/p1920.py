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


result = []
N = int(input())

A = input()
A = A.split(' ')
A = list(map(int, A))

M = int(input())

B = input()
B = B.split(' ')
A = list(map(int, A))
B = list(map(int, B))
left = 0
right = len(A) - 1
A.sort()

for B_ in B:
    out = b_search(A, B_, left, right)
    print(out)
