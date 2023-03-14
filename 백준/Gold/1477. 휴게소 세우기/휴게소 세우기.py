import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, l = map(int,input().split())

    rest = [0] + list(map(int,input().split())) + [l]
    rest.sort()

    left = 1
    right = l
    ans = 0
    while left <= right:

        mid = (left + right)//2

        cnt = 0

        for i in range(1, len(rest)):
            tmp = (rest[i] - rest[i-1])
            if tmp > mid:
                cnt += (tmp - 1) // mid


        if cnt > m:
            left = mid + 1
        else:
            ans = mid
            right = mid -1


    print(ans)