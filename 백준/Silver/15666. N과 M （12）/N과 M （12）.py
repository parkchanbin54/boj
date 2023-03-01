n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
s = []
def dfs(start):
    if start == m:
        print(' '.join(map(str, s)))
        return

    for i in range(len(nums)):
        if start == 0 or s[-1] <= nums[i]:
            s.append(nums[i])
            dfs(start+1)
            s.pop()

dfs(0)
