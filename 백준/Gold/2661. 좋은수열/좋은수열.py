import sys

def back_tracking(idx):
    for i in range(1, (idx//2) + 1):
        if tmp[-i:] == tmp[-2*i:-i]: return -1

    if idx == n:
        for i in range(n): print(tmp[i], end = '')
        return 0

    for i in range(1,4):
        tmp.append(i)
        if back_tracking(idx + 1) ==0:
            return 0
        tmp.pop()

if __name__ == '__main__':
    input = sys.stdin.readline
    tmp = []
    n = int(input())

    back_tracking(0)