import sys
from itertools import permutations

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    nums = [i for i in range(1,n+1)]
    per = permutations(nums,n)

    for pe in per:
        tmp = ""
        for p in pe:
            tmp += str(p)+" "
        print(tmp)
