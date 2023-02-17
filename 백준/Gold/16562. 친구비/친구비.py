import sys
from collections import deque


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, kk = map(int,input().split())

    f = list(map(int,input().split()))

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n+1)]
    ans = [[] for _ in range(n+1)]
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            ans[cnt].append(f[i-1])

            queue = deque()
            queue.append(i)

            while queue:
                c = queue.popleft()

                if len(graph[c]) == 0:
                    continue
                else:
                    for k in graph[c]:
                        if visited[k] == 0:
                            ans[cnt].append(f[k-1])
                            visited[k] = cnt
                            queue.append(k)

    answer = 0

    for i in range(1,n+1):
        if len(ans[i]) == 0:
            break
        else:
            answer += min(ans[i])

    if answer <= kk:
        print(answer)
    else:
        print("Oh no")
