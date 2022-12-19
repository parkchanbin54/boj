import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0
for i in s:
    i -= b
    cnt = 1
    if i > 0:
        cnt += i // c
        if i % c != 0:
            cnt += 1
    result += cnt
print(result)