import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
f = [0, 1]
for i in range(2, 21):
    f.append(f[i - 1] * i)
if s[0] == 1:
    k = s[1] - 1
    num = n - 1
    s = [i for i in range(1, n + 1)]
    result = []
    for _ in range(n - 1):
        result.append(s[k // f[num]])
        del s[k // f[num]]
        k %= f[num]
        num -= 1
    result.append(s[0])
    print(*result)
else:
    result = 0
    s = s[1:]
    num = n - 1
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if i == j: continue
            if s[i] > s[j]: cnt += 1
        for k in range(cnt):
            result += f[num]
        num -= 1
    print(result + 1)