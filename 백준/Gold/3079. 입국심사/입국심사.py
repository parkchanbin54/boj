import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    time = []
    for _ in range(n):
        time.append(int(input()))

    time.sort()

    left = 0
    right = time[0] * m

    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for t in time:
            cnt += mid // t

        if cnt < m:
            left = mid + 1
        else:
            right = mid

    print(right)