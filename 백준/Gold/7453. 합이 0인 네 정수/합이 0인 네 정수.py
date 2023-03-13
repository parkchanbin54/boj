import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    graph = [list(map(int,input().split())) for _ in range(n)]
    ab = []
    cd = []

    for i in range(n):
        for j in range(n):
            ab.append(graph[i][0] + graph[j][1])
            cd.append(graph[i][2] + graph[j][3])
    ab.sort()
    cd.sort()

    left = 0
    right = len(cd) -1
    cnt = 0
    while left < len(ab) and right >= 0:
        tmp = ab[left] + cd[right]
        if tmp == 0:
            nleft, nright = left + 1, right - 1
            while nleft < len(ab) and ab[nleft] == ab[left]:
                nleft += 1
            while nright >= 0 and cd[nright] == cd[right]:
                nright -= 1
            cnt += (nleft - left) * (right - nright)
            left, right = nleft , nright

        elif tmp > 0:
            right -= 1
        else:
            left += 1

    print(cnt)