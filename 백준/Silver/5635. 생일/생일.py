import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for _ in range(n):
        tmp = list(input().split())
        graph.append([tmp[0]] + list(map(int,tmp[1:])))

    graph.sort(key = lambda x : (x[3],x[2],x[1]))

    print(graph[-1][0])
    print(graph[0][0])