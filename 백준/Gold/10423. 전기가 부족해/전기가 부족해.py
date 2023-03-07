import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    vRoot = [i for i in range(n+1)]
    state = list(map(int,input().split()))

    for s in state:
        vRoot[s] = 0

    li = [list(map(int,input().split())) for _ in range(m)]
    li.sort(key = lambda x : x[2])
    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]

    ans = 0

    for a, b, w in li:
        aRoot = find(a)
        bRoot = find(b)
        if aRoot != bRoot:
            ans += w
            if aRoot > bRoot:
                vRoot[aRoot] = bRoot
            else:
                vRoot[bRoot] = aRoot


    print(ans)