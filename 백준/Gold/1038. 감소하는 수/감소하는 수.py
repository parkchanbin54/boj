import sys


def back_tracking(idx):
    ans.append(int(idx))
    for j in range(0, int(idx[-1])):
        back_tracking(idx + str(j))

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    ans = []

    if n > 1022:
        print(-1)
    else:
        for i in range(10):
            back_tracking(str(i))

        print(sorted(ans)[n])