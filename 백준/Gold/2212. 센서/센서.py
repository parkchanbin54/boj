import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    k = int(input())
    sensors = list(map(int,input().split()))
    sensors.sort()
    
    if k >= n:
        print(0)
        sys.exit()
    
    dis = []
    for i in range(1,n):
        dis.append((sensors[i] - sensors[i-1]))

    
    dis.sort(reverse= True)

    for i in range(k-1):
        dis.pop(0)

    print(sum(dis))

