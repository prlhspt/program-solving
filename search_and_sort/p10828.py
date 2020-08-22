import sys

read = sys.stdin.readline


def push(X):
    out.append(X)


def pop():
    if len(out) > 0:
        print(out.pop(len(out) - 1))
    else:
        print(-1)


def size():
    print(len(out))


def empty():
    if len(out) > 0:
        print(0)
    else:
        print(1)


def top():
    if len(out) > 0:
        print(out[len(out)-1])
    else:
        print(-1)


N = int(read())
out = []
for i in range(0, N):
    M = read().split()
    if M[0] == "push":
        push(M[1])
    elif M[0] == "pop":
        pop()
    elif M[0] == "size":
        size()
    elif M[0] == "empty":
        empty()
    elif M[0] == "top":
        top()
