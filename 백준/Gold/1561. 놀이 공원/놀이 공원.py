import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    time = list(map(int,input().split()))
    if n < m:
        print(n)
    else:
        left = 0
        right = 60000000000
        end = 0
        while left <= right:
            mid = (left + right) // 2
            cnt = m
            for t in time:
                cnt += mid // t
            if cnt >= n:
                right = mid - 1
                end = mid
            else:
                left = mid + 1

        cnt = m
        for t in time:
            cnt += (end-1) // t

        for i,t in enumerate(time):
            if end % t == 0:
                cnt += 1
            if cnt == n:
                print(i+1)
                break