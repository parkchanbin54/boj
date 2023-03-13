import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    ab, cd = [], []
    for i in range(n):
        for j in range(n):
            ab.append(graph[i][0] + graph[j][1])
            cd.append(graph[i][2] + graph[j][3])

    ab.sort()
    cd.sort()

    i, j = 0, len(cd) - 1
    result = 0
    while i < len(ab) and j >= 0:
        if ab[i] + cd[j] == 0:
            nexti, nextj = i + 1, j - 1

            while nexti < len(ab) and ab[nexti] == ab[i]:
                nexti += 1
            while nextj >= 0 and cd[nextj] == cd[j]:
                nextj -= 1

            result += (nexti - i) * (j - nextj)
            i, j = nexti, nextj
        elif ab[i] + cd[j] > 0:
            j -= 1
        else:
            i += 1

    print(result)