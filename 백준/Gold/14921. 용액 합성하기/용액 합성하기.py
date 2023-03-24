import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    liq = list(map(int,input().split()))

    liq.sort()

    left = 0
    right = n - 1
    ans = 1e9
    while left < right:
        tmp = liq[left] + liq[right]
        if tmp == 0:
            ans = 0
            break

        else:
            if abs(ans) > abs(tmp):
                ans = tmp
            if tmp < 0:
                left += 1
            else:
                right -= 1

    print(ans)
