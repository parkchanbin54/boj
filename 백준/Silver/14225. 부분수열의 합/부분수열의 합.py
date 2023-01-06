import sys
from itertools import combinations

if __name__ == '__main__':
    input = sys.stdin.readline
    S = int(input())

    nums = list(map(int,input().split()))

    check = [False for _ in range(2000001)]

    for i in range(1,S+1):
        tmp = combinations(nums, i)
        for n in tmp:
            check[sum(n)] = True

    for k in range(1,len(check)):
        if not check[k]:
            print(k)
            break