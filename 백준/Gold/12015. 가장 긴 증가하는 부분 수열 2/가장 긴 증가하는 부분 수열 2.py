import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

memo = [0]

for arr in array:
    if memo[-1] < arr:
        memo.append(arr)
    else:
        left = 0
        right = len(memo)

        while left < right:
            mid = (left+right)//2
            if memo[mid] < arr:
                left = mid + 1
            else:
                right = mid
        memo[right] = arr
print(len(memo)-1)
