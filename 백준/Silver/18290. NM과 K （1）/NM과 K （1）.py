import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, k = map(int,input().split())

    graph = [list(map(int,input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    ans = -1000000
    visited = [[False] * m for _ in range(n)]

    def back_tracking(px,py,ind,sum):
        global ans
        if ind == k:
            if sum > ans:
                ans = sum
            return

        for i in range(px,n):
            for j in range(py if i == px else 0, m):
                if not visited[i][j]:
                    flag = True
                    for b in range(4):
                        nx = i + dx[b]
                        ny = j + dy[b]

                        if 0 <= nx < n and 0 <= ny < m:
                            if visited[nx][ny]:
                                flag = False
                    if flag:
                        visited[i][j] = True
                        back_tracking(i,j,ind+1,sum+graph[i][j])
                        visited[i][j] = False

    back_tracking(0,0,0,0)
    print(ans)


