import sys
from itertools import combinations

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]

    members = list(i for i in range(n))
    answer = 1e9

    for i in range(1, n//2+1):
        min_diff = 1e9
        member = combinations(members, i)
        for m in member:
            start = list(m)
            link = list(set(members) - set(start))
            start_sum = 0
            link_sum = 0
            for j in range(len(start)):
                for k in range(len(start)):
                    start_sum += graph[start[j]][start[k]]

            for j in range(len(link)):
                for k in range(len(link)):
                    link_sum += graph[link[j]][link[k]]

            diff = abs(start_sum - link_sum)
            min_diff = min(min_diff, diff)

        answer = min(answer,min_diff)

    print(answer)
