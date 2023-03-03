import sys

sys.setrecursionlimit(10 ** 7)

def dfs(x):
    global ans
    visited[x] = True
    cycle.append(x)

    num = nums[x]

    if not visited[num]:
        return dfs(num)

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = [0] + list(map(int,input().split()))

        ans = 0
        visited = [False] * (n+1)

        for i in range(1,n+1):
            if not visited[i]:
                cycle = []
                dfs(i)
                ans += 1

        print(ans)