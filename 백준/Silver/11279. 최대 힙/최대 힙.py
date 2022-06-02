import sys
import heapq

heap = []
a = int(input())
for _ in range(a):
    b = int(sys.stdin.readline())
    if(b == 0):
        if (len(heap)==0):
            print(0)
            continue
        else:
            print(-1*heapq.heappop(heap))
    else:
        heapq.heappush(heap,-b)