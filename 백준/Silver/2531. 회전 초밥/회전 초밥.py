import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split()) 
cp1, cp2 = 0, k-1
sushi = []
for _ in range(N):
    sushi.append(int(input()))
check = set()

while cp1 < N:
    if cp2 >= N:
        cp2 -= N
    if cp2 < cp1:
        plates = sushi[cp1:] + sushi[:cp2+1]
    else:
        plates = sushi[cp1:cp2+1]
    cases = set(plates)
    if c not in cases:
        cases.add(c)
    if len(check) < len(cases):
        check = cases
    cp1 += 1
    cp2 += 1
print(len(check))