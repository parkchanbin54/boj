import sys
import heapq

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m, k = map(int,input().split())
    vRoot = [i for i in range(n+1)]
    state = list(map(int,input().split()))

    for s in state:
        vRoot[s] = 0

    graph = []

    for _ in range(m):
        a, b, c= map(int,input().split())
        graph.append((a,b,c))
    graph.sort(key = lambda x : x[2])
    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]
    ans = 0
    for i in range(m):
        a, b, w = graph[i]

        aRoot = find(a)
        bRoot = find(b)

        if aRoot != bRoot:
            if aRoot > bRoot:
                vRoot[aRoot] = bRoot
            else:
                vRoot[bRoot] = aRoot

            ans += w

    print(ans)



