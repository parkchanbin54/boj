import sys

sys.setrecursionlimit(10 ** 7)
def dfs(x):
    global ans
    vis[x] = True
    cycle.append(x)
    num = students[x]

    if vis[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        return dfs(num)


if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())

        students = [0] + list(map(int,input().split()))
        vis = [False] * (n+1)
        ans = []

        for i in range(n+1):

            if not vis[i]:
                cycle = []
                dfs(i)

        print(n - len(ans) + 1)