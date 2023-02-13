import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        a,b = map(int,input().split())
        graph.append((a,b))

    visit = [False for _ in range(1001)]

    graph.sort(key = lambda x : -x[1])

    ans = 0
    for days, worth in graph:
        i = days
        while i > 0 and visit[i]:
            i -= 1

        if i == 0:
            continue
        else:
            visit[i] = True
            ans += worth

    print(ans)