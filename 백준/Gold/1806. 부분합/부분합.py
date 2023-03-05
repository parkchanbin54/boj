import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, s = map(int,input().split())

    nums = list(map(int,input().split()))

    start = 0
    end = 0

    ans = 1e9
    tmp = 0
    while True:
        if tmp >= s:
            ans = min(ans,end-start)
            tmp -= nums[start]
            start += 1
        elif end == n:
            break
        else:
            tmp += nums[end]
            end += 1

    if ans == 1e9:
        print(0)
    else:
        print(ans)
