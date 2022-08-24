import sys
sys.setrecursionlimit(10**9)


# queen을 dfs 탐색
def dfs_queen(x, y, v):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] != "p" and graph[x][y] != "k":
        if graph[x][y] != "q":
            graph[x][y] = "x"

        if v == 0:
            dfs_queen(x + 1, y, 0)
        elif v == 1:
            dfs_queen(x - 1, y, 1)
        elif v == 2:
            dfs_queen(x, y + 1, 2)
        elif v == 3:
            dfs_queen(x, y - 1, 3)
        elif v == 4:
            dfs_queen(x + 1, y + 1, 4)
        elif v == 5:
            dfs_queen(x + 1, y - 1, 5)
        elif v == 6:
            dfs_queen(x - 1, y + 1, 6)
        elif v == 7:
            dfs_queen(x - 1, y - 1, 7)
        return True
    return False


# knight를 dfs 탐색(1번씩 탐색)
def dfs_knight(x, y):
    check(x + 2, y + 1)
    check(x + 2, y - 1)
    check(x - 2, y + 1)
    check(x - 2, y - 1)
    check(x + 1, y - 2)
    check(x - 1, y - 2)
    check(x + 1, y + 2)
    check(x - 1, y + 2)


def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] != "p" and graph[x][y] != "k" and graph[x][y] != "q":
        graph[x][y] = "x"
        return True
    return False


n, m = map(int, sys.stdin.readline().split())
queen = list(map(int, sys.stdin.readline().split()))
knight = list(map(int, sys.stdin.readline().split()))
pawn = list(map(int, sys.stdin.readline().split()))
graph = [["o"] * m for _ in range(n)]
cnt = 0

for q in range(1, queen[0] * 2, 2):
    nx, ny = queen[q] - 1, queen[q + 1] - 1
    graph[nx][ny] = "q"

for k in range(1, knight[0] * 2, 2):
    nx, ny = knight[k] - 1, knight[k + 1] - 1
    graph[nx][ny] = "k"

for p in range(1, pawn[0] * 2, 2):
    nx, ny = pawn[p] - 1, pawn[p + 1] - 1
    graph[nx][ny] = "p"

for i in range(n):
    for j in range(m):
        if graph[i][j] == "q":
            dfs_queen(i, j, 0)
            dfs_queen(i, j, 1)
            dfs_queen(i, j, 2)
            dfs_queen(i, j, 3)
            dfs_queen(i, j, 4)
            dfs_queen(i, j, 5)
            dfs_queen(i, j, 6)
            dfs_queen(i, j, 7)

        elif graph[i][j] == "k":
            dfs_knight(i, j)

for c in graph:
    cnt += c.count("o")

print(cnt)