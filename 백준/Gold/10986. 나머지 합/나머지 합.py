import sys
def input(): return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
nums = list(map(int,input().split()))
pSum = [0] * (n+1)

for i in range(1,n+1):
    pSum[i] = pSum[i-1] + nums[i-1]
nums = list(map(lambda x: x % m,nums))
pSum = list(map(lambda x: x % m, pSum))
count = [0] * m
for p_sum in pSum[1:]:
    count[p_sum] += 1
    
result = 0
for i in range(1,n+1):
    result += count[pSum[i-1]]
    count[pSum[i]] -= 1
print(result)