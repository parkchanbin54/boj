import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = []
    for _ in range(n):
        a,b = map(int,input().split())
        graph.append((a,b))

    graph.sort(key=lambda x: -x[1])

    visit = [False for _ in range(1001)]
    ans = 0

    for time, worth in graph:
        day = time

        while day > 0 and visit[day]:
            day -= 1

        if day == 0:
            continue
        else:
            visit[day] = True
            ans += worth
    print(ans)
