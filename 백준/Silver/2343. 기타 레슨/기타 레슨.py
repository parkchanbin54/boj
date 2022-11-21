import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    video = list(map(int,input().split()))

    vm = max(video)
    start = vm
    end = sum(video)

    res = 10 ** 9

    while(start <= end):
        mid = (start + end) // 2
        cnt = 1
        tmp = 0

        for i in range(n):
            if tmp + video[i] <= mid:
                tmp += video[i]
            else:
                cnt += 1
                tmp = video[i]
            if cnt > m:
                break
        if cnt > m:
            start = mid + 1
        else:
            end = mid - 1
            if mid >= vm:
                res = min(res, mid)
    print(res)
