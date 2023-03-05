import sys


if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input())
    check = [False] * (10 ** 7 + 1)
    for _ in range(t):
        n = int(input())

        nums = [input().rstrip() for _ in range(n)]
        nums.sort()
        flag = True
        for i in range(n-1):
            long = len(nums[i])
            if nums[i] == nums[i+1][:long]:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")