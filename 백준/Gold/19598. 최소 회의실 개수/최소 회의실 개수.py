import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    classes = []
    for _ in range(n):
        s, e = map(int,input().split())
        classes.append((s,e))

    classes.sort()
    queue = []

    heapq.heappush(queue,classes[0][1])

    for c in classes[1:]:
        if c[0] >= queue[0]:
            heapq.heappop(queue)
        heapq.heappush(queue,c[1])

    print(len(queue))