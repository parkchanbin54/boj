import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):

        n = int(input())
        dp = [1 for _ in range(10)]

        for i in range(n-1):
            for j in range(10):
                dp[j] = sum(dp[j:])

        print(sum(dp))


