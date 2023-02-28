import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    minheap = []
    maxheap = []
    ans = []

    for _ in range(n):
        t = int(input())

        if len(minheap) == len(maxheap):
            heapq.heappush(minheap,(-t,t))
        else:
            heapq.heappush(maxheap,(t,t))

        if maxheap and minheap[0][1] > maxheap[0][0]:
            min = heapq.heappop(maxheap)[0]
            max = heapq.heappop(minheap)[1]
            heapq.heappush(minheap,(-min,min))
            heapq.heappush(maxheap,(max,max))

        ans.append(minheap[0][1])

    for a in ans:
        print(a)