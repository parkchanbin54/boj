import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        coins = list(map(int,input().split()))
        m = int(input())

        check = [0] * (m + 1)
        for c in coins:
            if c > m:
                continue
            check[c] += 1
            for i in range(c+1,m+1):
                check[i] += check[i-c]

        print(check[m])

