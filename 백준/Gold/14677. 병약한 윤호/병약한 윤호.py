import sys
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().replace("\n",""))
dp = [[-501 for i in range((3*n)+1)] for k in range((3*n)+1)]
check = ["D","B","L"]
if s[0] == "B":
    dp[1][0] = 1
if s[-1] == "B":
    dp[0][1] = 1
for i in range(2,(3*n)+1):
    if s[-i] == check[i%3]:
        dp[0][i] = dp[0][i-1] + 1
    if s[i-1] == check[i%3]:
        dp[i][0] = dp[i-1][0] + 1
    for k in range(1,i):#k , i-k
        if s[k-1] == check[i%3] and s[-(i-k)] == check[i%3]:
            dp[k][i-k] = max(dp[k-1][i-k] , dp[k][i-k-1]) + 1
        elif s[k-1] == check[i%3]:
            dp[k][i-k] = dp[k-1][i-k] + 1
        elif s[-(i-k)] == check[i%3]:
            dp[k][i-k] = dp[k][i - k - 1] + 1
ans = 0
for i in dp:
    pp = max(i)
    ans = max(ans,pp)
print(ans)