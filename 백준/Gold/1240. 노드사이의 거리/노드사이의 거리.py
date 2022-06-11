from collections import deque
N, M = map(int, input().split())
link_arr = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, w = map(int, input().split())
    link_arr[n1].append((n2, w))
    link_arr[n2].append((n1, w))

for _ in range(M):
    s, e = map(int, input().split())
    def bfs(start, end):
        q = deque()
        q.append(start)
        visit = [-1] * (N + 1)
        visit[start] = 0
        while q:
            cur = q.popleft()
            if cur == end: break
            for adj_node, adj_dist in link_arr[cur]:
                if visit[adj_node] > -1: continue
                visit[adj_node] = visit[cur] + adj_dist
                q.append(adj_node)
        return visit[end]
    print(bfs(s, e))