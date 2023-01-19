import sys
from itertools import combinations

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    def GCD(a,b):
        while b!=0:
            a, b = b, a%b
        return a

    for _ in range(n):
        li = list(map(int,input().split()))
        coms = combinations(li[1:],2)
        ans = 0
        for com in coms:
            tmp = GCD(com[0],com[1])
            ans += tmp
        print(ans)


