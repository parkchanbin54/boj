import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        k,m,p = map(int,input().split())

        graph = [[] for _ in range(m+1)]
        degree = [0 for _ in range(m+1)]
        count = [[0,0] for _ in range(m+1)]
        dp = [ 0 for _ in range(m+1)]

        for _ in range(p):
            a, b = map(int,input().split())
            graph[a].append(b)
            degree[b] += 1

        queue = deque()

        for i in range(1,m+1):
            if degree[i] == 0:
                queue.append(i)
                dp[i] = i
                count[i] = [1,1]

        while queue:
            now = queue.popleft()
            dp[now] = count[now][0]
            if count[now][1] >= 2:
                dp[now] += 1

            for next in graph[now]:
                degree[next] -= 1
                if dp[now] == count[next][0]:
                    count[next][1] += 1
                elif dp[now] > count[next][0]:
                    count[next] = [dp[now], 1]
                if degree[next] == 0:
                    queue.append(next)

        print(str(k)+' '+str(dp[m]))