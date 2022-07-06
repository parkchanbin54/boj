import heapq
import sys

n = int(input())
heap = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(k), k))
