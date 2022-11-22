import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())

    relations = [[] for _ in range(n)]
    relations.sort()

    ans  = False

    visited = [False] * 2001

    for _ in range(m):
        a,b = map(int,input().split())
        relations[a].append(b)
        relations[b].append(a)

    def dfs(k, depth):
        global ans
        visited[k] = True

        if depth ==4:
            ans = True
            return
        for i in relations[k]:
            if not visited[i]:
                visited[i] = True
                dfs(i,depth + 1)
                visited[i] = False


    for i in range(n):
        dfs(i,0)
        visited[i] = False
        if ans:
            break

    if ans:
        print(1)
    else:
        print(0)



