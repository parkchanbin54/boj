import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, s = map(int,input().split())

    bros = list(map(int,input().split()))
    tmp = []
    for bro in bros:
        tmp.append(abs(bro - s))


    def GCD(a,b):
        while b != 0:
            a , b = b, a%b
        return a

    GCDnum = tmp[0]

    for i in range(1,len(tmp)):
        GCDnum = GCD(GCDnum, tmp[i])

    print(GCDnum)
