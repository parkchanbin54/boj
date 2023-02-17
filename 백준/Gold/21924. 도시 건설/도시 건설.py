import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int,input().split())

    vRoot = [i for i in range(N+1)]

    Elist = [list(map(int,input().split())) for _ in range(M)]
    Elist.sort(key = lambda x:x[2])
    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]
    ans = 0
    total = 0
    sol = []
    for s,e,w in Elist:
        sRoot = find(s)
        eRoot = find(e)
        total += w
        if sRoot != eRoot:
            if sRoot > eRoot:
                vRoot[sRoot] = eRoot
            else:
                vRoot[eRoot] = sRoot
            sol.append(w)
            ans += w

    if len(sol) == N-1:
        print(total - ans)
    else:
        print(-1)

