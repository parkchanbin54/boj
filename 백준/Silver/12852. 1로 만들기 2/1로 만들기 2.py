import sys
from collections import deque

if __name__ == '__main__':
    N = int(input())
    Q = deque()
    Q.append([N])
    answer = []

    while Q:
        arr = Q.popleft()

        x = arr[0]
        if x == 1:
            answer = arr
            break

        if x % 3 == 0:
            Q.append([x // 3] + arr)

        if x % 2 == 0:
            Q.append([x // 2] + arr)

        Q.append([x - 1] + arr)

    print(len(answer) - 1)
    answer.sort(reverse=True)
    print(" ".join(map(str,answer)))