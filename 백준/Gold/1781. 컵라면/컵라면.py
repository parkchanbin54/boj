import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    heap = []
    for i in range(1,n+1):
        s, w = map(int,input().split())
        heap.append((s,w))
        
    heap.sort()
    
    queue = []
    
    for i in heap:
        heapq.heappush(queue,i[1])
        if i[0] < len(queue):
            heapq.heappop(queue)
    
    print(sum(queue))