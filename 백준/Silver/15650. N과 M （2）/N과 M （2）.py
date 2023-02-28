import sys

def back_tracking(j):
    if len(tmp) == m:
        print(*tmp)
        return

    for i in range(j+1,n):
        tmp.append(nums[i])
        back_tracking(i)
        tmp.pop()

if __name__ == '__main__':
    input = sys.stdin.readline
    tmp = []
    n, m = map(int,input().split())

    nums = [i for i in range(1,n+1)]

    back_tracking(-1)