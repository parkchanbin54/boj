import sys


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    vRoot = [i for i in range(n+1)]
    graph = [list(map(int,input().split())) for _ in range(m)]

    graph.sort(key = lambda x: x[2])
    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]

    ans = 0
    li = []
    for s,e,w in graph:
        sRoot = find(s)
        eRoot = find(e)

        if sRoot != eRoot:
            if sRoot > eRoot:
                vRoot[sRoot] = eRoot
            else:
                vRoot[eRoot] = sRoot
            ans += w

    print(ans)
