import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    liq = list(map(int,input().split()))

    liq.sort()
    start= 0
    end = len(liq) -1
    m = abs(liq[start] + liq[end])
    ans = [liq[start], liq[end]]

    while start < end:
        tmp = liq[start] + liq[end]

        if m > abs(tmp):
            m = abs(tmp)
            ans = [liq[start], liq[end]]
            if m == 0:
                break
        if tmp < 0:
            start += 1
        else:
            end -= 1

    print(' '.join(map(str,ans)))