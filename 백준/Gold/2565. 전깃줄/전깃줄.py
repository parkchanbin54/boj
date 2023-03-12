import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    graph = []

    for _ in range(n):
        a, b = map(int,input().split())
        graph.append((a,b))

    graph.sort(key = lambda x : x[1])

    mem = [-1]

    for a,b in graph:
        if a > mem[-1]:
            mem.append(a)
        else:
            left = 0
            right = len(mem)

            while left < right:
                mid = (left + right)//2
                if mem[mid] < a:
                    left = mid + 1
                else:
                    right = mid

            mem[right] = a

    print(n - len(mem) + 1)

