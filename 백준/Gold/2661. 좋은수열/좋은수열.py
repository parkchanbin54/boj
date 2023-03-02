import sys

def back_tracking(idx):
    for i in range(1, (idx//2) + 1):
        if tmp[-i:] == tmp[-i*2:-i]: return -1

    if idx == n:
        print(''.join(tmp))
        return 0

    for i in range(1,4):
        tmp.append(str(i))
        if back_tracking(idx + 1) == 0:
            return 0
        tmp.pop()

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    tmp = []

    back_tracking(0)