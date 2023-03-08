import sys
def bitmask():
    global maxans

    for i in range(1 << n*m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + graph[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        for col in range(m):
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + graph[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxans = max(maxans, total)



if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    maxans = 0
    graph = [list(map(int,input().rstrip())) for _ in range(n)]

    bitmask()
    print(maxans)