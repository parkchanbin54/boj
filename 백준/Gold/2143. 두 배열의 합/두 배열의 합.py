import sys
import bisect

if __name__ == '__main__':
    input = sys.stdin.readline
    t, n = int(input()),int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

    Asum = []
    Bsum = []

    for i in range(n):
        s = a[i]
        Asum.append(s)
        for j in range(i+1,n):
            s+= a[j]
            Asum.append(s)

    for i in range(m):
        s = b[i]
        Bsum.append(s)
        for j in range(i+1,m):
            s += b[j]
            Bsum.append(s)

    Asum.sort()
    Bsum.sort()

    ans = 0

    for i in range(len(Asum)):
        l = bisect.bisect_left(Bsum, t-Asum[i])
        r = bisect.bisect_right(Bsum, t-Asum[i])
        ans += r - l

    print(ans)

