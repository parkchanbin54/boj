from collections import deque

start, end = map(int, input().split())
MAX=10**5
dist = [0]*(MAX + 1)
q= deque()
q.append(start)
while q:
    x=q.popleft()
    if x==end:
        print(dist[x])
        break
    for nx in (x-1 , x+1 , x *2):
        if 0<= nx <= MAX and not dist[nx]:
            dist[nx]= dist[x] +1
            q.append(nx)
