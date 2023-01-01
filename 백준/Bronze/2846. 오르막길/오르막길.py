
N = int(input())
numlist = list(map(int, input().split()))

pre = numlist[0]
high = 0
res = 0
for i in numlist:
    if pre < i:
        high += i - pre

    else:
        res = max(res, high)
        high = 0
    pre = i

print(max(high, res))