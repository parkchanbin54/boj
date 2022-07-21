import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

order = max(dp)
lst = []
print(order)
for i in range(n-1, -1, -1):
    if dp[i] == order:
        lst.append(array[i])
        order -= 1
lst.reverse()

for i in lst:
    print(i, end=' ')