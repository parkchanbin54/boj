import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int,input().split())

    gender = list(input().split())
    vRoot = [i for i in range(N+1)]

    Elist = [list(map(int,input().split())) for _ in range(M)]

    Elist.sort(key = lambda x : x[2])

    ans = 0
    sol = []

    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]



    for u,e,d in Elist:
        uRoot = find(u)
        eRoot = find(e)

        if uRoot != eRoot and gender[e-1] != gender[u-1]:
            if uRoot > eRoot:
                vRoot[uRoot] = eRoot
            else:
                vRoot[eRoot] = uRoot
            sol.append(d)
            ans += d

    if len(sol) != N-1:
        print(-1)
    else:
        print(ans)