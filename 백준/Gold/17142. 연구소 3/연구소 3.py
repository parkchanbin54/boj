import sys
from collections import deque
import copy


def back_tracking(idx):
    if len(tmp) == m:
        virus_set.append(copy.deepcopy(tmp))
        return

    for i in range(idx,len(virus_num)):
        if i not in tmp:
            tmp.append(i)
            back_tracking(i+1)
            tmp.pop()

def bfs():
    graph_copy = copy.deepcopy(graph)
    cnt = 0
    total = 0

    for g in graph_copy:
        total += g.count(0)

    while queue:
        cur_x, cur_y,d  = queue.popleft()
        fl = False

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph_copy[nx][ny] == 0 or graph_copy[nx][ny] == 2:
                    if graph_copy[nx][ny] == 0:
                        cnt += 1
                    graph_copy[nx][ny] = 3
                    queue.append((nx,ny,d+1))
            if cnt == total:
                break

    if cnt != total:
        return -1

    return d


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    virus = []

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    graph = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        graph.append(tmp)
        for j in range(n):
            if tmp[j] == 2:
                virus.append((i,j,0))

    virus_num = [i for i in range(len(virus))]
    virus_set = []
    tmp = []

    back_tracking(0)

    min = 1e9

    ans = []
    for i in range(len(virus_set)):
        queue = deque()
        for k in virus_set[i]:
            queue.append(virus[k])

        result = bfs()


        if min > result and result != -1:
            min = result

    if min == 1e9:
        min = -1
    print(min)