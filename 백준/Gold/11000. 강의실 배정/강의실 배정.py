import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    cl = [list(map(int,input().split())) for _ in range(N)]

    removed = 0

    cl.sort()
    room = []

    heapq.heappush(room, cl[0][1])

    for i in range(1,N):
        if room[0] > cl[i][0]:
            heapq.heappush(room, cl[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room,cl[i][1])

    print(len(room))
