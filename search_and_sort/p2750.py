import sys
read = sys.stdin.readline

A = []
N = int(read())
for i in range(0, N):
    A.append(read().strip())

A = list(map(int, A))
A = sorted(A)

for i in A:
    print(i)