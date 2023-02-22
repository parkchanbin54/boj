import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        t = int(input())
        files = list(map(int,input().split()))
        heap = []

        for file in files:
            heapq.heappush(heap,file)
        ans = 0
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            ans += (a+b)
            heapq.heappush(heap, a+b)

        print(ans)