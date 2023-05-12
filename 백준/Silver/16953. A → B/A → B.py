import sys

def dfs(a,l):
    global answer
    if a == b:
        answer = min(answer, l)
        return
    if a > b:
        return -1
    else:
        dfs(a*2, l+1)
        dfs(a*10+1, l+1)





if __name__ == '__main__':
    input = sys.stdin.readline
    answer = 1e9
    a, b = map(int,input().split())

    dfs(a,0)
    if answer == 1e9:
        print(-1)
    else:
        print(answer+1)
