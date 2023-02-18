import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    edges = [list(map(int,input().split())) for _ in range(m)]
    visited = [1e10] * (n+1)


    def bf(start):
        visited[start] = 0
        for i in range(n):
            for j in range(m):
                node = edges[j][0]
                next_node = edges[j][1]
                cost = edges[j][2]

                if visited[node] != 1e10 and visited[next_node] > visited[node] + cost:
                    visited[next_node] = visited[node] + cost

                    if i == n-1:
                        return True
        return False


    neg = bf(1)

    if neg:
        print(-1)
    else:
        for i in range(2,n+1):
            if visited[i] == 1e10:
                print(-1)
            else:
                print(visited[i])