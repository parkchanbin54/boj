import sys
def sum3():
    result = [1e9, 1e9, 1e9]
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            tmp = liq[i] + liq[l] + liq[r]
            if abs(sum(result)) > abs(tmp):
                result = [liq[i], liq[l], liq[r]]

            if tmp == 0:
                return liq[i], liq[l], liq[r]
            elif tmp > 0:
                r -= 1
            else:
                l += 1
    return result[0], result[1], result[2]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    liq = list(map(int,input().split()))


    liq.sort()
    print(' '.join(map(str,sum3())))

