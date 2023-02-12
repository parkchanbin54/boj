import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    boos = list(map(int,input().split()))

    tmp = [0 for i in range(1000001)]

    for boo in boos:
        if boo == 1000000:
            tmp[n] += 1
        else:
            if tmp[boo+1] != 0:
                tmp[boo+1] -= 1
            tmp[boo] += 1

    print(sum(tmp))
