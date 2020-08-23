import sys

read = sys.stdin.readline


def push_front(X):
    out.insert(0, X)


def push_back(X):
    out.append(X)


def pop_front():
    if len(out) > 0:
        print(out.pop(0))
    else:
        print(-1)


def pop_back():
    if len(out) > 0:
        print(out.pop())
    else:
        print(-1)


def size():
    print(len(out))


def empty():
    if len(out) > 0:
        print(0)
    else:
        print(1)


def front():
    if len(out) > 0:
        print(out[0])
    else:
        print(-1)


def back():
    if len(out) > 0:
        print(out[len(out) - 1])
    else:
        print(-1)


N = int(read())
out = []
for i in range(0, N):
    M = read().split()
    if M[0] == "push_front":
        push_front(M[1])
    elif M[0] == "push_back":
        push_back(M[1])
    elif M[0] == "pop_front":
        pop_front()
    elif M[0] == "pop_back":
        pop_back()
    elif M[0] == "size":
        size()
    elif M[0] == "empty":
        empty()
    elif M[0] == "front":
        front()
    elif M[0] == "back":
        back()
