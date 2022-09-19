import sys
input = sys.stdin.readline
n, m = map(int,input().split())

k = sorted(list(map(int, input().rstrip().split())))
temp = []

def sol(start):
    if len(temp) == m:
        print(' '.join(map(str, temp)))
        return
    for i in range(start, n):
        if k[i] not in temp:
            temp.append(k[i])
            sol(i + 1)
            temp.pop()


sol(0)