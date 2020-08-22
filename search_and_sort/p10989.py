import sys
read = sys.stdin.readline
write = sys.stdout.write
N = int(read())
cnt_list = [0] * 10001
for i in range(N):
    cnt_list[int(read().strip())] += 1

for i in range(10001):
    write("%s\n" % i * cnt_list[i])