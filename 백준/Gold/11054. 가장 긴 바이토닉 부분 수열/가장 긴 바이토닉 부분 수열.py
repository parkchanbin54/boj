import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
reverse_array = array[::-1]
inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if reverse_array[i] > reverse_array[j]:
            dec[i] = max(dec[i], dec[j]+1)
result = [0 for _ in range(n)]

for i in range(n):
    result[i] = inc[i] + dec[n-i-1]-1

print(max(result))