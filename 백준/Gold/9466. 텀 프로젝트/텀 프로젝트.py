import sys
sys.setrecursionlimit(10 ** 7)
def cycle(x):
    global ans

    visited[x] = True
    num = students[x]
    tmp.append(x)

    if visited[num]:
        if num in tmp:
            ans += len(tmp[tmp.index(num):])
            return
    else:
        return cycle(num)

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = 0
        students = [-1] + list(map(int,input().split()))

        visited = [False] * (n + 1)
        for i in range(1,n+1):
            if not visited[i]:
                tmp = []
                cycle(i)
        print(n - ans)
