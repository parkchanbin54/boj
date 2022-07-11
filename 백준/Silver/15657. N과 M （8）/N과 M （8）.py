import sys
input = sys.stdin.readline
n, m = map(int, input().split())

nums = list(map(int, input().split()))
s = []
nums.sort()

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start-1, n):
        s.append(nums[i])
        dfs(i+1)
        s.pop()

dfs(1)