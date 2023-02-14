import sys
import heapq
if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = []
    for _ in range(n):
        n,s,e = map(int,input().split())
        heapq.heappush(graph,(s,e,n))


    pq = []
    answer = 0
    s, e, n = heapq.heappop(graph)

    heapq.heappush(pq,e)
    while graph:
        s, e, n = heapq.heappop(graph)
        if pq[0] <= s:
            heapq.heappop(pq)
        heapq.heappush(pq,(e))

    print(len(pq))