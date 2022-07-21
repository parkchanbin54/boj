import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))

dp = []
dp.append(-1e9-1)
for arr in array:
    if arr > dp[-1]:
        dp.append(arr)
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right)//2
            if dp[mid] < arr:
                left = mid +1
            else:
                right = mid
        dp[right] = arr

print(len(dp)-1)