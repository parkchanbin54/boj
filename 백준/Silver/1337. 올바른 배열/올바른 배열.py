import sys
def sol():
    input = sys.stdin.readline
    n = int(input())

    graph = []

    for _ in range(n):
        tmp = int(input().rstrip())
        graph.append(tmp)

    graph.sort()

    result = 5
    for g in graph:
        s = 4
        for k in range(1,5):
            if g+k in graph:
                s -= 1
        if s < result:
            result = s

    print(result)

if __name__ == '__main__':
    sol()
