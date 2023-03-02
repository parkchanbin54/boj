import sys


def back_tracking(start):
    if len(tmp) == 5:
        return 0

    for x in graph[start]:
        if x not in tmp:
            tmp.append(x)
            if back_tracking(x) == 0:
                return 0
            tmp.pop()


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    graph = [[] for _ in range(n)]



    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)


    for i in range(n):
        tmp = [i]
        if back_tracking(i) == 0:
            print(1)
            break
    else:
        print(0)