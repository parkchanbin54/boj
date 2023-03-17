import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    arr = list(input().rstrip())
    l = len(arr)

    dp = [[0] * l for _ in range(l)]

    for i in range(l):
        for s in range(l - i):
            e = s + i

            if s == e:
                dp[s][e] = 1
            else:
                if arr[s] == arr[e]:
                    if s + 1 == e: dp[s][e] = 1
                    elif dp[s+1][e-1] == 1: dp[s][e] = 1
    result = [0] * l

    for i in range(l):
        for j in range(i+1):
            if dp[j][i]:
                if result[i] == 0 or result[i] > result[j-1] + 1:
                    result[i] = result[j-1] + 1


    print(result[l-1])
