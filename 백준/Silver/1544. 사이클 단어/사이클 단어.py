import sys
from collections import deque

N = int(sys.stdin.readline())
w_li = list()
for i in range(N):
    w_li.append(sys.stdin.readline().rstrip())

for i in range(N):
    dq = deque(w_li[i])
    while True:
        dq.append(dq.popleft())
        save = "".join(dq)
        if save == w_li[i]:
            break

        if save in w_li:
            idx = w_li.index(save)
            w_li.pop(idx)
            w_li.insert(idx, w_li[i])

w_li = set(w_li)
print(len(w_li))