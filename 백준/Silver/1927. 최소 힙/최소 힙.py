import heapq
import sys
heap = []
a = int(input())
for _ in range(a):
    b = int(sys.stdin.readline())
    if(b == 0):
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,b)
