import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int,input().split()))

    stack = []
    ans = [-1] * n

    stack.append(0)

    for i in range(1,n):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        stack.append(i)

    print(*ans)
