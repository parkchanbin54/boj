import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    F,S,G,U,D = map(int,input().split())
    checked = [1e9] * (F+1)
    cur = S
    count = 0
    move = [U,-D]
    queue = deque()
    queue.append(cur)
    checked[cur] = 0
    while queue:
        cur = queue.popleft()
        for i in range(2):
            ncur = cur + move[i]

            if 0 < ncur < (F + 1) and checked[ncur] == 1e9:
                queue.append(ncur)
                checked[ncur] = checked[cur] + 1

    if checked[G] == 1e9:
        print("use the stairs")
    else:
        print(checked[G])