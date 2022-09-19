import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

k = sorted(list(map(int,input().split())))
temp = []

def so():
    if len(temp) == m:
        print(' '.join(map(str,temp)))
        return
    else:
        for i in range(n):
            temp.append(k[i])
            so()
            temp.pop()


so()