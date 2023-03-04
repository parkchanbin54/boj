import sys

def dfs(x):
    visited[x] = True

    num = nums[x]
    if not visited[num]:
        return dfs(num)



if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = [0] +list(map(int,input().split()))

        visited = [False] * (n+1)
        cnt = 0
        for i in range(1,n+1):
            if not visited[i]:
                cycle = []
                dfs(i)
                cnt += 1

        print(cnt)