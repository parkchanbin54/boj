import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(day, late, absent):
    if late == 2 or absent == 3:
        return 0

    if day == n:
        return 1

    if dp[day][late][absent] == -1:
        attend = (
            dfs(day + 1, late, 0)
            + dfs(day + 1, late + 1, 0)
            + dfs(day + 1, late, absent + 1)
        )
        dp[day][late][absent] = attend
        return attend
    else:
        return dp[day][late][absent]


if __name__ == "__main__":
    n = int(input())
    dp = [[[-1 for absent in range(3)] for late in range(2)] for day in range(n)]
    print(dfs(0, 0, 0) % 1000000)