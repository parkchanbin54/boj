import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    nums = list(map(int,input().split()))
    cal = list(map(int,input().split()))

    up, down = -1e9,1e9

    tmp = [nums[0]]
    def back_tracking(t,l):
        global up
        global down

        if l == n:

            if t > up:
                up = t
            if t < down:
                down = t
            return

        for j in range(4):
            if cal[j] == 0:
                continue
            else:
                cal[j] -= 1
                if j == 0:
                    back_tracking(t+nums[l],l+1)
                elif j == 1:
                    back_tracking(t-nums[l],l+1)
                elif j == 2:
                    back_tracking(t*nums[l],l+1)
                else:
                    back_tracking(int(t/nums[l]),l+1)
                cal[j] += 1

    back_tracking(nums[0], 1)
    print(up, down)


