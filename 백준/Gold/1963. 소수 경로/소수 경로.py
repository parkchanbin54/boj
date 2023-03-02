import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    isprime = [False,False] + [True] * 9999

    for i in range(2,101):
        if isprime[i]:
            for j in range(i+i, 10001, i):
                isprime[j] = False

    for _ in range(n):
        a, b = input().split()
        queue = deque()
        queue.append((a,0))
        visited = [False] * 10001
        flag = False
        while queue:
            cur, d = queue.popleft()

            if cur == b:
                flag = True
                break

            for i in range(4):
                for j in range(10):
                    if i == 0 and j ==0:
                        continue
                    tmp = int(cur[:i]+str(j)+cur[i+1:])
                    if isprime[tmp] and not visited[tmp]:
                        visited[tmp] = True
                        queue.append((str(tmp),d+1))
        if flag:
            print(d)
        else:
            print(0)