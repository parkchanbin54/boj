import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())

    nums = list(map(int,input().split()))
    nums.sort()
    cnt = 0
    for i in range(n):
        tmp = nums[:i] + nums[i + 1:]
        left, right = 0, len(tmp) - 1

        while left < right:
            t = tmp[left] + tmp[right]

            if t < nums[i]:
                left += 1

            elif t == nums[i]:
                cnt += 1
                break

            else:
                right -= 1

    print(cnt)
