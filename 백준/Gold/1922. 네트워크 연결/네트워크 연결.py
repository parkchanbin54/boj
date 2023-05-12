import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    vRoot = [i for i in range(n+1)]
    graph = [list(map(int,input().split())) for _ in range(m)]
    graph.sort(key = lambda x : x[2])
    def find(x):
        if x != vRoot[x]:
            vRoot[x] = find(vRoot[x])
        return vRoot[x]

    answer = 0

    for a,b,w in graph:
        aRoot = find(a)
        bRoot = find(b)

        if aRoot != bRoot:
            if aRoot > bRoot:
                vRoot[aRoot] = bRoot
            else:
                vRoot[bRoot] = aRoot

            answer += w

    print(answer)