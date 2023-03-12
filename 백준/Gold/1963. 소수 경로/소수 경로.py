import sys
from collections import deque
def isprime():
    for i in range(2,100):
        if prime[i]:
            for j in range(i+i, 10000, i):
                prime[j] = False

def sol(c):
    queue = deque()
    queue.append((c,0))
    flag = False
    while queue:
        cur, d = queue.popleft()
        if cur == b:
            flag = True
            break

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                tmp = int(cur[:i] + str(j) + cur[i+1:])
                if prime[tmp] and not visited[tmp]:
                    visited[tmp] = True
                    queue.append((str(tmp), d+1))
    if flag:
        print(d)
    else:
        print(0)






if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    prime = [False,False] + [True] * 9999
    isprime()

    for _ in range(n):
        visited = [False for _ in range(10000)]
        a,b = input().rstrip().split()
        sol(a)