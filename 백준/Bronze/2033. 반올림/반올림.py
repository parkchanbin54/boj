N = int(input())
d = 10
while N > d:
    if N % d >= d // 2:
        N += d
    N -= (N % d)
    d *= 10
print(N)