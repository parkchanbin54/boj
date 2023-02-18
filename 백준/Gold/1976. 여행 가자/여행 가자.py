import sys


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]

    vRoot = [i for i in range(n)]
    sch = list(map(int,input().split()))

    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]

    flag = True

    def union(x, y):
        xRoot = find(x)
        yRoot = find(y)

        if xRoot != yRoot:
            if xRoot > yRoot:
                vRoot[xRoot] = yRoot
            else:
                vRoot[yRoot] = xRoot

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(i,j)






    vRoot = [-1] + vRoot
    start = vRoot[sch[0]]

    for i in range(1,m):
        if vRoot[sch[i]] != start:
            print("NO")
            break
    else:
        print("YES")
