import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    k = int(input())

    if k >= n:
        print(0)
        sys.exit()

    sensors = list(map(int,input().split()))
    sensors.sort()
    dis = []

    for i in range(1,n):
        dis.append((sensors[i] - sensors[i-1]))

    dis.sort()

    for _ in range(k-1):
        dis.pop()

    print(sum(dis))