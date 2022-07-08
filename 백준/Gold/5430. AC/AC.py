import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    tmp = input()
    t = int(input())
    arr2 = input().rstrip()[1:-1].split(",")
    arr = deque(arr2)
    if t == 0:
        arr = []
    count = 0
    flag = True
    for j in tmp:
        if j == 'R':
            count += 1
        if j == 'D':
            if len(arr) == 0:
                print("error")
                flag = False
                break
            if count % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if flag:
        if count % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
