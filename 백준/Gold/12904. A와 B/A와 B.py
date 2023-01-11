import sys

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    S = list(input().rstrip())
    T = list(input().rstrip())

    def dfs(t):
        if t == S:
            print(1)
            sys.exit(0)

        if len(t) == 0:
            return 0

        if t[-1] == 'A':
            dfs(t[:-1])
        if t[-1] == 'B':
            dfs(t[:-1][::-1])

    dfs(T)
    print(0)