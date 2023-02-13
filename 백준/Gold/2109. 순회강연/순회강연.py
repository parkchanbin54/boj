import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        a, b = map(int,input().split())
        graph.append([a,b])

    graph.sort(key = lambda x : (-x[0]))

    visit = [False for _ in range(10001)]
    ans = 0
    for wor, day in graph:
        i = day

        while i > 0 and visit[i]:
            i -= 1

        if i == 0:
            continue
        else:
            ans += wor
            visit[i] = True


    print(ans)