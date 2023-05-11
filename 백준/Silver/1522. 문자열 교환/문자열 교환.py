S = input()
a = S.count('a')

ans = len(S)
for i in range(a - 1, len(S)):
    ans = min(ans, S[i - a + 1:i + 1].count('b'))

for i in range(0, a - 1):
    ans = min(ans, (S[i - a + 1:] + S[:i + 1]).count('b'))

print(ans)