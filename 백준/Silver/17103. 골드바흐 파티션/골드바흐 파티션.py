import sys
import math

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    inf = 1000000
    isprime = [False, False] + [True] * (inf -1)
    
    for i in range(2,int(math.sqrt(inf))+1):
        if isprime[i]:
            for j in range(i+i,inf,i):
                isprime[j] = False

    for _ in range(n):
        t = int(input())

        start = t//2
        end = t//2
        ans = 0
        while start >= 0 and end <= t:
            if isprime[end] and isprime[start]:
                ans += 1
            start -= 1
            end += 1

        print(ans)