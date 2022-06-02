n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0

for i in range(1, n):
    arr[i] += arr[i - 1]
print(sum(arr))
