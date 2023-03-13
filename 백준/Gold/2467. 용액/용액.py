import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    liq = list(map(int,input().split()))
    liq.sort()

    left = 0
    right = n - 1

    tmp = abs(liq[left] + liq[right])
    ans = [liq[left] , liq[right]]

    while left < right:

        if abs(liq[left] + liq[right]) < tmp:
            tmp = abs(liq[left] + liq[right])
            ans = [liq[left],liq[right]]
            if tmp == 0:
                break
        if liq[left] + liq[right] < 0:
            left += 1
        else:
            right -=1

    print(' '.join(map(str,ans)))
