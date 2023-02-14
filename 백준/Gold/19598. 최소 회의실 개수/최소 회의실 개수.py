import sys
import heapq
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    heap = []
    for _ in range(n):
        s, e = map(int,input().split())
        heapq.heappush(heap,(s,e))


    pq = []
    s, e = heapq.heappop(heap)
    heapq.heappush(pq,e)

    while heap:
        s, e = heapq.heappop(heap)
        if pq[0] <= s:
            heapq.heappop(pq)
        heapq.heappush(pq,e)

    print(len(pq))