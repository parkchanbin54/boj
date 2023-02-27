import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, k = map(int,input().split())
        times = [0] + list(map(int,input().split()))

        graph = [[] for _ in range(n+1)]
        degree = [0 for _ in range(n+1)]
        dp = [0 for _ in range(n+1)]
        for _ in range(k):
            a, b = map(int,input().split())
            graph[a].append(b)
            degree[b] += 1

        queue = deque()

        for i in range(1,n+1):
            if degree[i] == 0:
                queue.append(i)
                dp[i] = times[i]

        while queue:
            tmp = queue.popleft()
            for i in graph[tmp]:
                degree[i] -= 1
                dp[i] = max(dp[tmp] + times[i], dp[i])
                if degree[i] == 0:
                    queue.append(i)
        w = int(input())
        print(dp[w])
