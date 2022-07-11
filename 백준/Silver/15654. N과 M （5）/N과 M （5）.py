import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(n):
        if nums[i] in s:
            continue
        s.append(nums[i])
        dfs(i+1)
        s.pop()
dfs(0)