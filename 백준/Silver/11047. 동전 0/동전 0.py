import sys
input = sys.stdin.readline
n, m = map(int, input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))
count = 0 
for i in reversed(range(n)):
    count += m//coin[i]
    m = m%coin[i]
print(count)
