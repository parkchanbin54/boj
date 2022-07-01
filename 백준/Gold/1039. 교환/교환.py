from collections import deque
from itertools import combinations
import sys, copy

input = sys.stdin.readline

def bfs():
    c = set()
    ans = 0
    qlen = len(q)
    while qlen:
        x = q.popleft()
        l = list(str(x))
        for i, j in d:
            s = copy.deepcopy(l)
            temp_i, temp_j = s[i], s[j]
            s[i], s[j] = temp_j, temp_i
            if s[0] == '0':
                continue
            nx = int(''.join(s))
            if nx not in c:
                ans = max(ans, nx)
                c.add(nx)
                q.append(nx)
        qlen -= 1
    return ans

n, k = map(int, input().split())
item = [i for i in range(len(str(n)))]
d = list(combinations(item, 2))
q = deque()
q.append(n)

ans = 0
while k:
    ans = bfs()
    k -= 1
if not ans:
    print(-1)
else:
    print(ans)