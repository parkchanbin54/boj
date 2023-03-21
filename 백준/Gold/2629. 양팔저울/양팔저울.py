import sys

def cal(num,w):
    if num > n:
        return

    if dp[num][w]:
        return

    dp[num][w] = 1

    cal(num+1,w)
    cal(num+1,w+k[num-1])
    cal(num+1,abs(w - k[num-1]))

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    k = list(map(int, input().split()))
    t = int(input())
    t = list(map(int,input().split()))

    dp = [[0 for j in range((i+1)*500+1)] for i in range(n+1)]
    r = []

    cal(0,0)

    for i in t:
        if i > 30 * 500:
            r.append('N')
            continue
        if dp[n][i] == 1:
            r.append('Y')
        else:
            r.append('N')

    print(*r)