import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    nums = list(map(int,input().split()))

    dict = defaultdict(int)

    for num in nums:
        dict[num] += 1

    tmp = []

    for num in nums:
        tmp.append([num,dict[num]])

    stack = []

    ans = [-1] * n
    stack.append(0)
    for i in range(1,n):
        while stack and tmp[stack[-1]][1] < tmp[i][1]:
            ans[stack.pop()] = tmp[i][0]
        stack.append(i)

    print(*ans)