import sys
import heapq

if __name__ == '__main__':
    input = sys.stdin.readline

    n, k = map(int,input().split())

    pq = []
    for _ in range(n):
        wei, wor = map(int,input().split())
        pq.append([wei,wor])

    for _ in range(k):
        bag = int(input())
        pq.append([bag,-1])

    pq.sort(key = lambda x : (x[0], -x[1]))

    ans = 0
    prev_list = []

    for i in range(len(pq)):
        if pq[i][1] == -1:
            tmp = i
            if len(prev_list) == 0:
                continue
            wei = -heapq.heappop(prev_list)
            ans += wei

        else:
            heapq.heappush(prev_list,(-pq[i][1]))

    print(ans)
