import sys
t = int(input())
s = []
for i in range(t):
    s.append(int(sys.stdin.readline()))
s.sort(reverse=True)
istrue = False
for i in range(len(s) - 2):
    if s[i] < s[i + 1] + s[i + 2]:
        print(s[i] + s[i + 1] + s[i + 2])
        istrue = True
        break
if istrue == False:
    print(-1)