import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        n, m = map(int,input().split())
        if n == 0 and m == 0:
            break
        graph = [list(map(int,input().split())) for _ in range(m)]

        graph.sort(key = lambda x : x[2])
        vRoot = [i for i in range(n)]

        def find(x):
            if x != vRoot[x]:
                vRoot[x] = find(vRoot[x])
            return vRoot[x]

        ans = 0
        for a,b,c in graph:
            aRoot = find(a)
            bRoot = find(b)

            if aRoot != bRoot:
                if aRoot > bRoot:
                    vRoot[aRoot] = bRoot
                else:
                    vRoot[bRoot] = aRoot
            else:
                ans += c

        print(ans)