import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        days = int(input())
        charts = list(map(int,input().split()))
        ans = 0
        max = 0
        for i in range(days-1, -1, -1):
            if charts[i] > max:
                max = charts[i]
            else:
                ans += max - charts[i]

        print(ans)

