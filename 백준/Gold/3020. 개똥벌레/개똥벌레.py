import sys
from collections import defaultdict

if __name__ == '__main__':
    input = sys.stdin.readline

    n, h = map(int,input().split())
    down = [0] * (h+1)
    up = [0] * (h+1)

    m_count = n
    cnt = 0

    for i in range(n):
        tmp = int(input())
        if i % 2 == 0:
            down[tmp] += 1
        else:
            up[tmp] += 1

    for i in range(h-1,0,-1):
        down[i] += down[i+1]
        up[i] += up[i+1]

    for i in range(1,h+1):
        if m_count > (down[i] + up[h-i+1]):
            m_count = (down[i] + up[h-i+1])
            cnt = 1
        elif m_count == (down[i] + up[h-i+1]):
            cnt += 1

    print(m_count, cnt)


