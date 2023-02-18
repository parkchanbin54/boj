import sys


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    vRoot = [i for i in range(n)]

    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x != y:
            if x > y:
                vRoot[x] = y
            else:
                vRoot[y] = x


    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in range(n):
            if tmp[j] == 1:
                union(i,j)


    vRoot = [-1] + vRoot
    sch = list(map(int,input().split()))
    start = vRoot[sch[0]]

    for i in range(1,m):
        if vRoot[sch[i]] != start:
            print("NO")
            break
    else:
        print("YES")