from collections import deque
import sys 

if __name__ == '__main__':
    input = sys.stdin.readline

    n, w, L = map(int, input().split())

    trucks = list(map(int,input().split()))

    truck = []

    bridge_trucks = deque()
    seq = 0
    result = 0

    while True:
        if seq == n and not bridge_trucks:
            break
        if seq < n:
            if sum(bridge_trucks) + trucks[seq] <= L:
                bridge_trucks.append(trucks[seq])
                truck.append(0)
                seq += 1
        result += 1
        for i in range(len(bridge_trucks)):
            truck[i] += 1
        if truck[0] == w:
            bridge_trucks.popleft()
            del truck[0]


    print(result+1)