import sys

if __name__ == '__main__':
    input =sys.stdin.readline

    n = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]
    graph.sort()
    graph_y =[0] + [graph[i][1] for i in range(n)]
    graph_x = [0] + [graph[i][0] for i in range(n)]

    mem = [-1]
    dp = [0] * (n+1)
    ans = []

    for i in range(1,n+1):
        if mem[-1] < graph_y[i]:
            mem.append(graph_y[i])
            dp[i] = len(mem) - 1
        else:
            left = 0
            right = len(mem) - 1

            while left < right:
                mid = (left + right)//2

                if mem[mid] < graph_y[i]:
                    left = mid + 1
                else:
                    right = mid
            dp[i] = right
            mem[right] = graph_y[i]

    m = max(dp)
    for i in range(n,0,-1):
        if dp[i] == m:
            graph_x.remove(graph[i-1][0])
            m -= 1



    print(n - len(mem) + 1)
    for i in range(1,len(graph_x)):
        print(graph_x[i])




