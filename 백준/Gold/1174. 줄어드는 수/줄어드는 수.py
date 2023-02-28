import sys

def back_tracking(cur):
    ans.append(int(cur))
    for j in range(0,int(cur[-1])):
        back_tracking(cur + str(j))


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    if n > 1023:
        print(-1)
    else:
        ans = []
        for i in range(10):
            back_tracking(str(i))

        print(sorted(ans)[n-1])