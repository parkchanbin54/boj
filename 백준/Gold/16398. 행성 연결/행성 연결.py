import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    N = int(input())

    graph = [list(map(int,input().split())) for _ in range(N)]

    vRoot = [i for i in range(N+1)]

    Elist = []
    for i in range(N):
        for j in range(i, N):
            if graph[i][j] != 0:
                Elist.append([i,j,graph[i][j]])


    Elist.sort(key = lambda x : x[2])


    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]


    ans = 0

    for s,e,w in Elist:
        sRoot = find(s)
        eRoot = find(e)

        if sRoot != eRoot:
            if sRoot > eRoot:
                vRoot[sRoot] = eRoot
            else:
                vRoot[eRoot] = sRoot

            ans += w


    print(ans)