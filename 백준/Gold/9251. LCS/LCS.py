import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()

dp =[0 for _ in range(len(b))]

for i in range(len(a)):
    check = 0
    for j in range(len(b)):
        if check < dp[j]:
            check = dp[j]
        elif a[i] == b[j]:
            dp[j] = check + 1

print(max(dp))