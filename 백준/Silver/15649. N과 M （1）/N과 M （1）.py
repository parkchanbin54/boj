import sys
def back_tracking():
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(len(nums)):
        if nums[i] not in tmp:
            tmp.append(nums[i])
            back_tracking()
            tmp.pop()


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int,input().split())
    tmp = []
    nums = [i for i in range(1,n+1)]

    back_tracking()