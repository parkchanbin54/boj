import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    N, P = map(int,input().rstrip().split())

    line = [[0] for _ in range(7)]

    result = 0

    for i in range(N):
        n, p = map(int,input().rstrip().split())

        while line[n][-1] > p:
            line[n].pop()
            result += 1

        if line[n][-1] == p:
            continue

        line[n].append(p)
        result += 1

    print(result)